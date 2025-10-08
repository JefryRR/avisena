from pydantic import BaseModel, Field
from typing import Optional

class FincaBase(BaseModel):
    nombre_finca: str= Field(min_length=3, max_length=70)
    longitud: float
    latitud: float
    id_usuario: int
    estado_finca: bool

class FincasCreate(FincaBase):
    pass

class FincaUpdate(BaseModel):
    nombre_finca: Optional[str] = Field(default=None, min_length=3, max_length=70)
    longitud: Optional[float] = None
    latitud: Optional[float] = None
    

class FincaEstado(BaseModel):
    estado_finca: Optional[bool] = None

class FincaOut(FincaBase):
    id_finca: int
    nombre: str
