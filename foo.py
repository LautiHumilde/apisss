import os
import requests
import json
from pprint import pprint
from dotenv import load_dotenv

# Cagro todo
load_dotenv()

def main():
    api = os.getenv("IMDB_API_KEY")
    
#comprovacion
    if api is None:
        print("No tenes clave")
        return

    # solicitud
    nombrePeli = input("ingresa alguna pelicula o serie: ")
    url = f"http://www.omdbapi.com/?apikey={api}&t={nombrePeli}"

#guardo la sespuesta en mi variable respuesta y eso lo paso a json en mi variable datos
    respuesta = requests.get(url)
    datos = respuesta.json()

#pregunto si me dieron respesta
    if datos.get("Response") == "True":
        pprint(datos)
        # me da todo
    else:
        print("sin resultado")

if __name__ == "__main__":
    main()
