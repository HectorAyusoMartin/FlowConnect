#Nombre del proyecto: FlowConnect 
#Autor: Héctor Ayuso Martín



#FlowConnect fue elegido como nombre porque resalta la fluidez en la conexión entre backend y frontend.


'''
Confifuracion de main.
Nucelo de la API.
'''

from fastapi import FastAPI

aplicacion = FastAPI()


#Creando un endpoint para hacer pruebas..:

@aplicacion.get('/')

def leer_raiz():
    return {'Mensaje' : 'FlowConnect está funcionando correctamente'}


