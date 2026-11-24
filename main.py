import json

with open("config/lima.json", encoding="utf-8") as archivo:
    configuracion = json.load(archivo)

print(configuracion["ciudad"])