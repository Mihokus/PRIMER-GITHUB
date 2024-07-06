from FUNCIONES_SEBASTIAN_RODRIGUEZ_005 import *

BASE_DATOS = []
print("¡Bienvenido al programa de TODOAHORRO!")
print("Las opciones disponibles son: ")

while True:
    menu()
    opcion = input("\nIngrese la opcion a realizar: ")

    if opcion == "1":
        REGISTAR_CLIENTE(BASE_DATOS)

    elif opcion == "2":
        LISTA_DE_CLIENTES(BASE_DATOS)

    elif opcion == "3":
        REGISTAR_COMPRA(BASE_DATOS)

    elif opcion == "4":
        LISTA_DE_COMPRAS_CLIENTE(BASE_DATOS)

    elif opcion == "5":
        print("Hasta la proxima!")
        break

    else:
        print("\nSeleccione una opcion disponible\n")