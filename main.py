# from fastapi import FastAPI
# from pydantic import BaseModel


# app = FastAPI()

# #Esquema
# class Item(BaseModel):
#     nombre: str
#     precio: float
#     estado: bool


# @app.get('/')
# def inicio():
#     mensaje = "Hola mundo"
#     nombre = "Jeferson Rios"
#     return {
#         "mensaje": mensaje,
#         "nombre":nombre
#         }

# @app.get('/suma')
# def suma(num1:int, num2:int):
#     resultado = num1+num2
#     return {
#         "mensaje": f"sumar {num1} y {num2} ",
#         "resultado": resultado}



# @app.get('/prueba')
# def potencia(num:int):
#     resultado = num**3
#     return {"mensaje": f"el número {num} al cubo es:",
#             "resultado": resultado
#             }

# @app.post('/guardar-producto')
# def guardar_producto(producto: Item, cantidad: int):
#     total =producto.precio*cantidad

#     return {"mensaje":"almacenado con éxito", "nombre":producto.nombre, "precio": producto.precio,"total": total}

# #crear una lista de diccionarios vacía global, un esquema llamdo aprendiz que pida el nombre, la edad, el correo y la ficha
# #Crear un endpoint que recibe ese esquema, almacenando el la lista vacía y que retorne la lista de los estudiantes almacenado
# estudiantes = []


# class Aprendices(BaseModel):
#     nombre_estudiante: str
#     n_documento: int
#     edad: int
#     correo: str
#     ficha:int


# @app.post('/aprendices')
# def datos_estudiantes(estudiante:Aprendices):
#     estudiantes.append(estudiante)
#     return estudiantes  

# @app.put('/aprendices')
# def datos_estudiantes(nombre: str, documento:int, edad_est:int, correo_est:str, ficha_est:int):
#     for actualizar_est in estudiantes:
#         if documento == actualizar_est.n_documento:
#             actualizar_est.nombre_estudiante = nombre
#             actualizar_est.edad = edad_est
#             actualizar_est.correo = correo_est
#             actualizar_est.ficha = ficha_est
#     return estudiantes

# @app.delete('/eliminar_aprendiz')
# def datos_estudiantes(documento:int):
#     indice = 0
#     for i, eliminar_est in enumerate(estudiantes):
#         if documento == eliminar_est.n_documento:
#             indice = i
    
#     if indice != 0:
#         del estudiantes[indice]
#     return estudiantes


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import estates, isolation
from app.router import users
from app.router import auth

app = FastAPI()

# Incluir en el objeto app los routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(estates.router, prefix="/estates", tags=["estates"])
app.include_router(isolation.router, prefix="/isolations", tags=["aislamiento"])

app.include_router(auth.router, prefix="/access", tags=["login"])



# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP
    allow_headers=["*"],  # Permitir cualquier encabezado en las solicitudes
)

@app.get("/")
def read_root():
    return {
                "message": "ok",
                "autor": "ADSO 2925889"
            }
