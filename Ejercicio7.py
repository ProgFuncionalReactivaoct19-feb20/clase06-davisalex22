"""
@davisalex22

    Programación Funcional
        Funciones Puras
        Efectos Secundarios
"""
# Importacion csv
import csv

# Lectura de datos con DictReader.
def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter="\t")

with open("data/trabajadores.csv") as midata:
    lista = list(lineasDiccionario(midata))
    
    # Filtrar las listas cuyos paises sean mayores a 10 letras.
    funcion1 = filter(lambda x: len(list(x.items())[2][1])>= 10, lista)
    
    # Ordenar conforme el día de nacimiento.
    print(list(sorted(funcion1, key = lambda x: list(x.items())[1][1].split("-")[2])))


 
