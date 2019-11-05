"""
@davisalex22

    Programación Funcional
        Funciones Puras
        Efectos Secundarios
"""
import csv


def lineas(archivo):
    return csv.reader(archivo, delimiter=";")


with open("data/data-estudiantes.csv") as midata:
    lista = list(lineas(midata))

    print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email", lista))))
