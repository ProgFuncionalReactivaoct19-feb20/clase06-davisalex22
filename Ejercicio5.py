"""
@davisalex22

    Programación Funcional
        Funciones Puras
        Efectos Secundarios
"""
import csv


def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter=";")


with open("data/data-estudiantes.csv") as midata:
    lista = list(lineasDiccionario(midata))
    # print(list(lista))
    
    print(list(map(lambda x : list(x.items())[0][1], lista)))
