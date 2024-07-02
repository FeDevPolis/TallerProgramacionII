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

# Programa principal
nombres_y_apellidos = obtener_nombres_y_apellidos()
lista1, lista2 = repartir_aleatoriamente(nombres_y_apellidos)

print("Grupo 1:", lista1)
print("Grupo 2:", lista2)
