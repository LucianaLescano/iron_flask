from config.configuration import db
from config.configuration import collection



def insertamensaje(escena, personaje, frase):
    '''
    Función que inserta los datos en mongo, es el momento de revisar que todos los 
    datos esten como queramos.
    '''
    dict_insert = {
        "scene" : f"{escena}",
        "character_name" : f"{personaje}",
        "dialogue" : f"{frase}"
    }
    collection.inset_one(dict_insert)