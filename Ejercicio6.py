"""
@davisalex22

    Programación Funcional
        Funciones Puras
        Efectos Secundarios
"""
# Importar csv
import csv

# Lectura de archivo con DictReader
def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
    lista = list(lineasDiccionario(midata))
    
    # Uso de concatenación de distintas posiciones con el uso de funciones
    print(list(map(lambda x: "%s - %s" % (list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lista)))
