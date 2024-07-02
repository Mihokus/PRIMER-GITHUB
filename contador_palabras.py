"""
Cree un programa al cual se le entrega 
un texto (string) y te devuelva una lista 
impresa en pantalla con todas las palabras
unicas que tiene dicho texto, y al costado 
su frecuencia.
EJEMPLO1:
texto = 'hola como estas bien y tu bien'

LISTA EN PANTALLA:
- hola: 1
- como: 1
- estas: 1
- bien: 2
- y: 1
- tu: 1

EJEMPLO2:
texto = 'hola hola hola quien esta molestando'

LISTA EN PANTALLA:
- hola: 3
- quien: 1
- esta: 1
- molestando: 1


AYUDA:

texto = "hola como estas"

SPLIT:
lista_palabas = texto.split(" ")
lista_palabras --> ["hola", "como", "estas"]

UPPER:
texto_mayus = texto.upper()
texto_mayus --> "HOLA COMO ESTAS"
"""

### VAMOS A INICIAR ENTREGANDO LA CADENA DE TEXTO QUE VAMOS A ANALIZAR

Texto = input("Ingrese una cadena de texto para analizar: \n >")

#SE TRANSFORMA EL TEXTO POR PALABRAS EN UNA LISTA CON SUS PALABRAS, SPLIT LO UTILIZAMOS PARA SEPARAR LAS PALABRAS A TRAVES DE LO QUE SE INGRESE DENTRO DEL LOS PARENTESIS.
lista_de_texto = Texto.split(" ")

#VAMOS A ELIMINAR PALABRAS REPETIDAS A TRAVES DE  CONJUNTOS, CON LA FUNCION SET QUE NOS CONVIERTE LA LISTA EN UN CONJUNTO EN DONDE NO SE REPETIRAN LAS PALABRAS.
Palabras_texto = set(lista_de_texto)

#DEFINIMOS UN DICCIONARIO CONTADOR DE PALABRAS PARA PODER ALMACENARLOS.
Contador_palabras = {}

for palabras in Palabras_texto:
    Contador_palabras[palabras] = 0 

#AHORA DEBEMOS CONTAR LAS PALABRAS
for palabra in Palabras_texto:
    for p in lista_de_texto:
        if palabra == p:
            Contador_palabras[palabras] += 1
for llave, valor in Contador_palabras.items():
    print(f"{llave}:{valor}")
