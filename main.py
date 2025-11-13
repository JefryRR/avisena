from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import categories, estates, incidentes_genrales, inventory, isolation, registro_sensores, sensor_types, sensors, sheds
from app.router import users
from app.router import auth

app = FastAPI()

# Incluir en el objeto app los routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(estates.router, prefix="/estates", tags=["estates"])
app.include_router(isolation.router, prefix="/isolations", tags=["aislamiento"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(incidentes_genrales.router, prefix="/indidentes_Grals", tags=["indidentes_Grals"])
app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
app.include_router(registro_sensores.router, prefix="/registro_sensores", tags=["registro_sensores"])
app.include_router(sensor_types.router, prefix="/sensor_types", tags=["sensor_types"])
app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
app.include_router(sheds.router, prefix="/sheds", tags=["sheds"])

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
