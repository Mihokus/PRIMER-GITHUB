def menu():
    opciones = [
        "Registrar Cliente",
        "Listar Clientes Registrados",
        "Registrar Compra",
        "Listar Compras de un Cliente",
        "Salir del programa"
    ]

    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")

def REGISTAR_CLIENTE(BASE_DATOS):

    nombre = input("Ingrese el nombre del cliente: ").upper()

    apellido = input("Ingrese el apellido del cliente: ").upper()

    correo = input("Ingrese el correo electronico del cliente: ")

    id = len(BASE_DATOS) + 1

    BASE_DATOS.append({
        "NOMBRE": nombre,
        "APELLIDO": apellido,
        "CORREO": correo,
        "ID": id,
        "COMPRAS": []
    })

    print(f"\nSe ha almacenado correctamente al cliente con ID {id}\n")


def LISTA_DE_CLIENTES (BASE_DATOS):
    print(f"\nID\t\tNOMBRE\t\t\t\tCORREO\n")
    for clientes in BASE_DATOS:
        print(f'\n{clientes["ID"]}\t\t{clientes["NOMBRE"]} {clientes["APELLIDO"]}\t\t{clientes["CORREO"]}\n')
    
    print("\nSe genero correctamente la lista de clientes.\n")


def REGISTAR_COMPRA(BASE_DATOS):
    id = int(input("Ingrese el ID del cliente a ingresar una compra: "))
    for clientes in BASE_DATOS:
        if clientes["ID"] == id:
            fecha = input("Ingrese la fecha de la compra en formato AAAA-MM-DD: ")
            total = int(input("Ingrese el monto total de la compra: "))
            puntos = round(total * 0.01)
            clientes["COMPRAS"].append({
                "FECHA":fecha,
                "TOTAL":total,
                "PUNTOS ACUMULADOS": puntos
            })
            print("\nSe registro correctamente la compra.\n")
    

def LISTA_DE_COMPRAS_CLIENTE(BASE_DATOS):

    id = int(input("Ingrese el ID del cliente al que dese enviar el informe: "))
    texto = ""
    for clientes in BASE_DATOS:
        if clientes["ID"] == id:
            texto = f'\nID CLIENTE: {clientes["ID"]}\n'
            texto += f'\nNOOMBRE CLIENTE: {clientes["NOMBRE"]} {clientes["APELLIDO"]}\n'
            texto += '\nFECHA DE COMPRA\t\t\tTOTAL\t\t\tPUNTOS\n'
            for compra in clientes["COMPRAS"]:
                texto += f'\n{compra["FECHA"]}\t\t\t{compra["TOTAL"]}\t\t\t{compra["PUNTOS ACUMULADOS"]}\n'
                puntos_total = 0
                puntos_total += compra["PUNTOS ACUMULADOS"]
                texto += f'\nPUNTOS TOTAL A CANJEAR: {puntos_total}\n'
        
        with open(f"RESUMEN_CLIENTE_ID_{id}.txt","w") as archivo:
            archivo.write(texto)
        print("\nSe ha generado correctamente el informe de puntos acumulados.\n")
        break