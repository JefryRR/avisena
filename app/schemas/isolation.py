import datetime
from pydantic import BaseModel
from typing import Optional

class IsolationBase(BaseModel):
    id_incidente_gallina : int
    id_galpon: int

class IsolationCreate(IsolationBase):
    pass

class IsolationUpdate(BaseModel):
    id_incidente_gallina: Optional[int] = None
    id_galpon: Optional[int] = None
    

class IsolationEstado(BaseModel):
    pass

class IsolationOut(IsolationBase):
    fecha_hora: datetime.datetime
    id_aislamiento: int
    nombre: str
