#Generar un programa que almacene en una lista Nombres y Apellidos cargados 
#por el usuario hasta que decida no cargar más. 
#def obtener_nombres_y_apellidos()
#Después una vez obtenida la lista completa cuando el usuario decide no cargar
#más datos por medio del método def repartir_aleatoriamente(lista), realizar
#lo que sugiere el nombre del método, obteniendo como devolución dos listas,
#lista1 y lista2.
#Finalmente definir otro método que guarde los resultados obtenidos en un
#archivo *.txt. Una vez ejecutado, el programa debe imprimir en pantalla que los 
#resultados fueron guardados en el archivo 

import random

def obtener_nombres_y_apellidos():
    lista_completa = []
    while True:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        lista_completa.append((nombre, apellido))
        
        continuar = input("¿Desea cargar más nombres y apellidos? (s/n): ").lower()
        if continuar != 's':
            break
    return lista_completa

def repartir_aleatoriamente(lista):
    random.shuffle(lista)
    mitad = len(lista) // 2
    lista1 = lista[:mitad]
    lista2 = lista[mitad:]
    return lista1, lista2

def guardar_en_archivo(lista1, lista2, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Grupo 1:\n")
        for nombre, apellido in lista1:
            archivo.write(f"{nombre} {apellido}\n")
        
        archivo.write("\nGrupo 2:\n")
        for nombre, apellido in lista2:
            archivo.write(f"{nombre} {apellido}\n")

# Programa principal
nombres_y_apellidos = obtener_nombres_y_apellidos()
lista1, lista2 = repartir_aleatoriamente(nombres_y_apellidos)
nombre_archivo = "grupos_final.txt"

guardar_en_archivo(lista1, lista2, nombre_archivo)

print(f"Las listas se han guardado en el archivo {nombre_archivo}.")
