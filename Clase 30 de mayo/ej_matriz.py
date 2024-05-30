# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: en cada fila 
# el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. 
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing? 
# Partirás de: 
# matriz = [ 
#     [1, 5, 1],
#     [2, 1, 2],
#     [3, 0, 1],
#     [1, 4, 4]
# ]
#Debes llegar a: 
# matriz = [ 
#     [1, 5, 1, 7],
#     [2, 1, 2, 5],
#     [3, 0, 1, 4],
#     [1, 4, 4, 9]
# ]
# Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista





# Matriz inicial
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

# Modificamos cada fila para que el cuarto elemento sea la suma de los tres primeros
for fila in matriz:
    suma = sum(fila[:3])  # Sumamos los tres primeros elementos usando slicing
    fila.append(suma)  # Añadimos la suma como cuarto elemento

# Imprimimos la matriz resultante
print(matriz)