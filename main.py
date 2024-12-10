#Nombre del proyecto: FlowConnect 
#Autor: Héctor Ayuso Martín



#FlowConnect fue elegido como nombre porque resalta la fluidez en la conexión entre backend y frontend.


'''
Confifuracion de main.
Nucelo de la API.
'''

from fastapi import FastAPI

aplicacion = FastAPI()


#Creando datos ficticios

usuarios = [
    
{'id_usuario' : 1 , 'nombre' : 'Ayuso' , 'edad' : 33 , 'ubicacion' : 'Barcelona'},
{'id_usuario' : 2 , 'nombre' : 'Alberto' , 'edad' : 60 , 'ubicacion' : 'Valladolid'},
{'id_usuario' : 3 , 'nombre' : 'Reyes' , 'edad' : 62 , 'ubicacion' : 'Soria'},

]

transacciones = [
    
{'id_transiccion' : 1 , 'id_usuario': 1 , 'monto': 150.99, 'fecha':'2024-12-10'},
{'id_transiccion' : 2 , 'id_usuario': 2 , 'monto': 89.99, 'fecha':'2024-12-09'},
{'id_transiccion' : 3 , 'id_usuario': 1 , 'monto': 45.50, 'fecha':'2024-12-08'},





]


#Creando un endpoint para hacer pruebas..: endpoint: Raiz

@aplicacion.get('/')

def leer_raiz():
    return {'Mensaje' : 'FlowConnect está funcionando correctamente'}


#Endpoint Lista de usuarios:

@aplicacion.get('/usuarios')
def obtener_usuarios():
    return usuarios

#Endpoint para Lista de transacciones:

@aplicacion.get('/transacciones')
def obtener_transacciones():
    return transacciones
