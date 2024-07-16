import random
import cvs
def menu():
    opciones = [
        "Asignar sueldos aleatorios",
        "Clasificar sueldos",
        "Ver estadísticas",
        "Reporte de sueldos",
        "Salir del programa"
    ]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}.{opcion}")
        
    print("\n")

def asignar_sueldos(trabajadores):


def clasificar_datos(trabajadores):
    print(f"Sueldos menores a $800.000 TOTAL: {}\n")
    print(f"Nombre empleado\t\t\tSueldo")
    print(f"\t\t\t")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {}\n")
    print(f"Nombre empleado\t\t\tSueldo")
    print(f"\t\t\t") 
    print(f"Sueldos superiores a $2.000.000 TOTAL: {}\n")
    print(f"Nombre empleado\t\t\tSueldo")
    print(f"\t\t\t")

def estadisticas():
    print(f"El sueldo mas alto es: {}")
    print(f"El sueldo mas bajo es: {}")
    print(f"El promedio de sueldos es de {}")
    print(f"La media geometrica es de {}")


def reporte_sueldos():
    texto = "Nombre empleao\t\t\tSueldo Base\t\t\tDescuento AFP\t\t\tSUELDO LIQUIDO"
    with open('Analisis_de_datos.cvs','w', encoding='uft -8') as archivo:
        archivo.write(texto)

