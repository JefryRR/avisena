from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional
import logging

from app.schemas.estates import FincasCreate, FincaUpdate

logger = logging.getLogger(__name__)

def create_finca(db: Session, finca: FincasCreate) -> Optional[bool]:
    try:
        query = text("""
            INSERT INTO fincas (
                nombre, longitud, latitud,
                id_usuario, estado
            ) VALUES (
                :nombre, :longitud, :latitud,
                :id_usuario, :estado
            )
        """)
        db.execute(query, finca.model_dump())
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al crear la finca: {e}")
        raise Exception("Error de base de datos al crear la finca")


def get_finca_by_id(db: Session, id_finca: int):
    try:
        query = text("""SELECT id_finca, nombre, longitud, latitud,
                    fincas.id_usuario, estado, usuarios.nombre
                    FROM fincas 
                    INNER JOIN usuarios ON usuarios.id_usuario = fincas.id_usuario
                    WHERE id_finca = :finca_id""")
        result = db.execute(query, {"finca_id": id_finca}).mappings().first()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener finca por id: {e}")
        raise Exception("Error de base de datos al obtener la finca")

def get_all_fincas(db: Session):
    try:
        query = text("""SELECT id_finca, nombre, longitud, latitud,
                    fincas.id_usuario, estado, usuarios.nombre
                    FROM fincas 
                    INNER JOIN usuarios ON usuarios.id_usuario = fincas.id_usuario
                    """)
        result = db.execute(query).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error al obtener las fincas: {e}")
        raise Exception("Error de base de datos al obtener las fincas")

def update_finca_by_id(db: Session, finca_id: int, finca:FincaUpdate) -> Optional[bool]:
    try:
        # Solo los campos enviados por el cliente
        finca_data = finca.model_dump(exclude_unset=True)
        if not finca_data:
            return False  # nada que actualizar

        # Construir dinámicamente la sentencia UPDATE
        set_clauses = ", ".join([f"{key} = :{key}" for key in finca_data.keys()])
        sentencia = text(f"""
            UPDATE fincas 
            SET {set_clauses}
            WHERE id_finca = :id_finca
        """)

        # Agregar el id_usuario
        finca_data["id_finca"] = finca_id

        result = db.execute(sentencia, finca_data)
        db.commit()
        return result.rowcount > 0
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error al actualizar finca {finca_id}: {e}")
        raise Exception("Error de base de datos al actualizar la finca")
    
