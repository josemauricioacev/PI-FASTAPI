import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Importar todos los routers
from app.routers import (
    usuarios, aplicacion, categorias, seccion, 
    desarrollador, status, paises, generos,
    version_app, valoracion, notificaciones, 
    mis_apps, descargas, busqueda, descubrimiento,
    estadisticas, app_seccion, aplicacion_categorias,
    apps_desarrollador
)

app = FastAPI(
    title="SUSTAINITY API",
    description="API",
    version="1.0.0"
)

# Incluir todos los routers con sus prefijos
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(aplicacion.router, prefix="/aplicaciones", tags=["Aplicaciones"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorías"])
app.include_router(seccion.router, prefix="/secciones", tags=["Secciones"])
app.include_router(desarrollador.router, prefix="/desarrolladores", tags=["Desarrolladores"])
app.include_router(status.router, prefix="/status", tags=["Status"])
app.include_router(paises.router, prefix="/paises", tags=["Países"])
app.include_router(generos.router, prefix="/generos", tags=["Géneros"])
app.include_router(version_app.router, prefix="/versiones", tags=["Versiones"])
app.include_router(valoracion.router, prefix="/valoraciones", tags=["Valoraciones"])
app.include_router(notificaciones.router, prefix="/notificaciones", tags=["Notificaciones"])
app.include_router(mis_apps.router, prefix="/mis-apps", tags=["Mis Apps"])
app.include_router(descargas.router, prefix="/descargas", tags=["Descargas"])
app.include_router(busqueda.router, prefix="/busqueda", tags=["Búsqueda"])
app.include_router(descubrimiento.router, prefix="/descubrimiento", tags=["Descubrimiento"])
app.include_router(estadisticas.router, prefix="/estadisticas", tags=["Estadísticas"])
app.include_router(app_seccion.router, prefix="/app-seccion", tags=["App-Sección"])
app.include_router(aplicacion_categorias.router, prefix="/app-categorias", tags=["App-Categorías"])
app.include_router(apps_desarrollador.router, prefix="/apps-desarrollador", tags=["Apps-Desarrollador"])

@app.get("/")
def root():
    return {"message": "Lana App Store API funcionando correctamente"}