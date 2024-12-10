#Nombre del proyecto: FlowConnect 
#Autor: Héctor Ayuso Martín



#FlowConnect fue elegido como nombre porque resalta la fluidez en la conexión entre backend y frontend.


from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from datetime import datetime

aplicacion = FastAPI()

usuarios = [
    
    {"id_usuario": 1, "nombre": "Ayuso", "edad": 33, "ubicacion": "Madrid"},
    {"id_usuario": 2, "nombre": "Lydia", "edad": 28, "ubicacion": "Barcelona"},
    {"id_usuario": 3, "nombre": "Merche", "edad": 45, "ubicacion": "Sevilla"},
    {"id_usuario": 4, "nombre": "Carlos", "edad": 38, "ubicacion": "Valencia"},
    {"id_usuario": 5, "nombre": "Sofía", "edad": 22, "ubicacion": "Bilbao"},
    {"id_usuario": 6, "nombre": "Alberto", "edad": 50, "ubicacion": "Granada"},
    {"id_usuario": 7, "nombre": "Marina", "edad": 30, "ubicacion": "Zaragoza"},
    {"id_usuario": 8, "nombre": "Diego", "edad": 41, "ubicacion": "Alicante"},
    {"id_usuario": 9, "nombre": "Carmen", "edad": 29, "ubicacion": "Málaga"},
    {"id_usuario": 10, "nombre": "Javier", "edad": 36, "ubicacion": "Santander"}
]


transacciones = [
    
    
    {"id_transaccion": 1, "id_usuario": 1, "monto": 150.75, "fecha": "2024-12-10"},
    {"id_transaccion": 2, "id_usuario": 2, "monto": 89.99, "fecha": "2024-12-09"},
    {"id_transaccion": 3, "id_usuario": 4, "monto": 45.50, "fecha": "2024-12-08"},
    {"id_transaccion": 4, "id_usuario": 5, "monto": 200.30, "fecha": "2024-12-07"},
    {"id_transaccion": 5, "id_usuario": 1, "monto": 125.99, "fecha": "2024-12-06"},
    {"id_transaccion": 6, "id_usuario": 6, "monto": 75.20, "fecha": "2024-12-05"},
    {"id_transaccion": 7, "id_usuario": 1, "monto": 250.00, "fecha": "2024-12-04"},
    {"id_transaccion": 8, "id_usuario": 7, "monto": 320.50, "fecha": "2024-12-03"},
    {"id_transaccion": 9, "id_usuario": 10, "monto": 95.70, "fecha": "2024-12-02"},
    {"id_transaccion": 10, "id_usuario": 8, "monto": 140.80, "fecha": "2024-12-01"},
    {"id_transaccion": 11, "id_usuario": 5, "monto": 300.00, "fecha": "2024-11-30"},
    {"id_transaccion": 12, "id_usuario": 1, "monto": 80.65, "fecha": "2024-11-29"},
    {"id_transaccion": 13, "id_usuario": 6, "monto": 59.30, "fecha": "2024-11-28"},
    {"id_transaccion": 14, "id_usuario": 3, "monto": 230.00, "fecha": "2024-11-27"},
    {"id_transaccion": 15, "id_usuario": 1, "monto": 180.20, "fecha": "2024-11-26"},
    {"id_transaccion": 16, "id_usuario": 4, "monto": 99.99, "fecha": "2024-11-25"},
    {"id_transaccion": 17, "id_usuario": 9, "monto": 40.50, "fecha": "2024-11-24"},
    {"id_transaccion": 18, "id_usuario": 7, "monto": 220.00, "fecha": "2024-11-23"},
    {"id_transaccion": 19, "id_usuario": 8, "monto": 90.99, "fecha": "2024-11-22"},
    {"id_transaccion": 20, "id_usuario": 1, "monto": 120.75, "fecha": "2024-11-21"},
    {"id_transaccion": 21, "id_usuario": 10, "monto": 150.50, "fecha": "2024-11-20"},
    {"id_transaccion": 22, "id_usuario": 5, "monto": 60.20, "fecha": "2024-11-19"},
    {"id_transaccion": 23, "id_usuario": 1, "monto": 200.00, "fecha": "2024-11-18"},
    {"id_transaccion": 24, "id_usuario": 8, "monto": 130.75, "fecha": "2024-11-17"},
    {"id_transaccion": 25, "id_usuario": 6, "monto": 50.00, "fecha": "2024-11-16"},
    {"id_transaccion": 26, "id_usuario": 7, "monto": 100.99, "fecha": "2024-11-15"},
    {"id_transaccion": 27, "id_usuario": 9, "monto": 75.50, "fecha": "2024-11-14"},
    {"id_transaccion": 28, "id_usuario": 2, "monto": 90.00, "fecha": "2024-11-13"},
    {"id_transaccion": 29, "id_usuario": 4, "monto": 300.50, "fecha": "2024-11-12"},
    {"id_transaccion": 30, "id_usuario": 1, "monto": 99.99, "fecha": "2024-11-11"},
    {"id_transaccion": 31, "id_usuario": 10, "monto": 40.00, "fecha": "2024-11-10"},
    {"id_transaccion": 32, "id_usuario": 5, "monto": 250.99, "fecha": "2024-11-09"},
    {"id_transaccion": 33, "id_usuario": 6, "monto": 80.50, "fecha": "2024-11-08"},
    {"id_transaccion": 34, "id_usuario": 8, "monto": 220.75, "fecha": "2024-11-07"},
    {"id_transaccion": 35, "id_usuario": 7, "monto": 310.00, "fecha": "2024-11-06"},
    {"id_transaccion": 36, "id_usuario": 1, "monto": 99.99, "fecha": "2024-11-05"},
    {"id_transaccion": 37, "id_usuario": 2, "monto": 110.00, "fecha": "2024-11-04"},
    {"id_transaccion": 38, "id_usuario": 4, "monto": 130.50, "fecha": "2024-11-03"},
    {"id_transaccion": 39, "id_usuario": 1, "monto": 99.99, "fecha": "2024-11-02"},
    {"id_transaccion": 40, "id_usuario": 3, "monto": 70.75, "fecha": "2024-11-01"},
    
]


def validar_fecha(fecha: str):
    try:
        return datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Formato de fecha inválido: {fecha}. Usa YYYY-MM-DD.")

@aplicacion.get("/")
def leer_raiz():
    return {"mensaje": "¡FlowConnect está funcionando!"}

@aplicacion.get("/usuarios")
def obtener_usuarios():
    return usuarios

@aplicacion.get("/transacciones")
def obtener_transacciones(
    id_usuario: Optional[int] = Query(None, description="Filtrar por ID de usuario"),
    fecha_inicio: Optional[str] = Query(None, description="Filtrar desde esta fecha (YYYY-MM-DD)"),
    fecha_fin: Optional[str] = Query(None, description="Filtrar hasta esta fecha (YYYY-MM-DD)")
):
    resultado = transacciones

    if id_usuario is not None:
        resultado = [t for t in resultado if t["id_usuario"] == id_usuario]
        if not resultado:
            raise HTTPException(status_code=404, detail=f"No se encontraron transacciones para el usuario con ID {id_usuario}.")

    if fecha_inicio:
        fecha_inicio_dt = validar_fecha(fecha_inicio)
        resultado = [t for t in resultado if datetime.strptime(t["fecha"], "%Y-%m-%d") >= fecha_inicio_dt]
    
    if fecha_fin:
        fecha_fin_dt = validar_fecha(fecha_fin)
        resultado = [t for t in resultado if datetime.strptime(t["fecha"], "%Y-%m-%d") <= fecha_fin_dt]

    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron transacciones en el rango especificado.")

    return resultado
