from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.router.dependencies import get_current_user
from app.crud.permisos import verify_permissions
from sqlalchemy.exc import SQLAlchemyError
from core.database import get_db
from app.schemas.estates import FincasCreate, FincaOut, FincaUpdate
from app.schemas.users import UserOut
from app.crud import estates as crud_estates

router = APIRouter()
modulo = 3

@router.post("/crear", status_code=status.HTTP_201_CREATED)
def create_estate(
    finca: FincasCreate, 
    db: Session = Depends(get_db),
    user_token: UserOut = Depends(get_current_user)):
    try:
        id_rol = user_token.id_rol
        if not verify_permissions(db, id_rol, modulo, "insertar"):
            raise HTTPException(status_code=401, detail="Usuario no autorizado")

        crud_estates.create_finca(db, finca)
        
        return {"message": "Finca creada correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/by-id",response_model=FincaOut)
def get_finca(id: int, db: Session = Depends(get_db),
            user_token: UserOut = Depends(get_current_user)):
    try:
        finca = crud_estates.get_finca_by_id(db, id)
        if not finca:
            raise HTTPException(status_code=404, detail="Finca no encontrada")
        return finca
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/all_fincas",response_model=list[FincaOut])
def get_finca(
    db: Session = Depends(get_db),
    user_token: UserOut = Depends(get_current_user)):
    try:
        id_rol = user_token.id_rol
        if not id_rol ==1 or id_rol == 2:
            raise HTTPException(status_code=401, detail="Usuario no autorizado")

        finca = crud_estates.get_all_fincas(db)
        return finca

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/by_id/{finca_id}")
def update_estate(finca_id: int, finca: FincaUpdate, db: Session = Depends(get_db),
                user_token: FincaOut = Depends(get_current_user)):
    try:
        success = crud_estates.update_finca_by_id(db, finca_id, finca)
        if not success:
            raise HTTPException(status_code=400, detail="No se pudo actualizar la finca")
        return {"message": "Finca actualizada correctamente"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))


