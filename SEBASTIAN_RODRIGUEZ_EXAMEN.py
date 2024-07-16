from SEBASTIAN_RODRIGUEZ_FUNCIONES import *
import random
import cvs

trabajadores =["Juan Pérez",
               "María García",
               "Carlos López",
               "Ana Martínez",
               "Pedro Rodríguez",
               "Laura Hernández",
               "Miguel Sánchez",
               "Isabel Gómez",
               "Francisco Díaz",
               "Elena Fernández"]
sueldos = [
]

print("Bienvenido al analizador de datos\n")
while True:
    print("Opcines disponibles a realizar:")

    menu()

    opciones = input("Ingresa la opcion a realizar: ")

    if opciones == "1":
        asignar_sueldos(trabajadores)
    elif opciones == "2":
        clasificar_datos(trabajadores)
    elif opciones == "3":
        estadisticas(trabajadores)
    elif opciones == "4":
        reporte_sueldos(trabajadores):
    elif opciones == "5":
        print("Finalizando programa...")
        print("Desarrollado por Sebastian Rodriguez")
        print("RUT 20.598.479-8")
        break

