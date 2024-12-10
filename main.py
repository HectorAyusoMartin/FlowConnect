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
]

transacciones = [
    {"id_transaccion": 1, "id_usuario": 1, "monto": 150.75, "fecha": "2024-12-10"},
    {"id_transaccion": 2, "id_usuario": 2, "monto": 89.99, "fecha": "2024-12-09"},
    {"id_transaccion": 3, "id_usuario": 1, "monto": 45.50, "fecha": "2024-12-08"},
]

def validar_fecha(fecha: str):
    try:
        return datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Formato de fecha inválido: {fecha}. Usa YYYY-MM-DD.")

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

@aplicacion.get("/usuarios/{id_usuario}")
def obtener_usuario_por_id(id_usuario: int):
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usuario:
            return usuario
    raise HTTPException(status_code=404, detail=f"Usuario con ID {id_usuario} no encontrado.")

@aplicacion.get("/transacciones/{id_transaccion}")
def obtener_transaccion_por_id(id_transaccion: int):
    for transaccion in transacciones:
        if transaccion["id_transaccion"] == id_transaccion:
            return transaccion
    raise HTTPException(status_code=404, detail=f"Transacción con ID {id_transaccion} no encontrada.")
