#Consigna
#A partir de una lista realizar las siguientes tareas sin modificar la lista original:
#Borrar los elementos duplicados
#Ordenar la lista de mayor a menor
#Eliminar todos los números impares (  for ---- if (%2==1) ---- pop, remove   )
#Realizar una suma de todos los números que quedan (sum(lista))
#Añadir como primer elemento de la lista la suma realizada insert(0, suma)
#Devolver la lista modificada
#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
#lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
#Nota: Recuerda que para sumar todos los números de una lista puedes usar sum


def modificar_lista(lista):
    # Crear una copia de la lista original para no modificarla
    lista_copia = lista.copy()
    
    # Borrar los elementos duplicados
    lista_sin_duplicados = list(set(lista_copia))
    
    # Ordenar la lista de mayor a menor
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    
    # Eliminar todos los números impares
    lista_pares = [num for num in lista_ordenada if num % 2 == 0]
    
    # Realizar una suma de todos los números que quedan
    suma_pares = sum(lista_pares)
    
    # Añadir como primer elemento de la lista la suma realizada
    lista_pares.insert(0, suma_pares)
    
    # Devolver la lista modificada
    return lista_pares

# Lista original
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Llamar a la función y obtener la lista modificada
lista_modificada = modificar_lista(lista)

# Verificar que la suma de todos los números a partir del segundo concuerda con el primer número de la lista
if sum(lista_modificada[1:]) == lista_modificada[0]:
    print("La suma de todos los números a partir del segundo concuerda con el primer número de la lista.")
else:
    print("La suma de todos los números a partir del segundo NO concuerda con el primer número de la lista.")

# Imprimir la lista modificada
print(lista_modificada)