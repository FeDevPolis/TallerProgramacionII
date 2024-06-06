# Inicializa una tupla llamada tupla_prueba con tuplas 
# anidadas como sus elementos.
# Inicializa una lista llamada claves que contiene las claves 
# deseadas para el diccionario de salida.
# Inicializa una lista vacía llamada resultado para almacenar 
# los diccionarios resultantes.
# Inicia un bucle for para iterar sobre cada tupla anidada 
# en tupla_prueba.
# Para cada tupla anidada, inicializa un diccionario vacío 
# llamado sub_dict.
# Inicia un bucle anidado for usando la función range para 
# iterar sobre el rango de la longitud de claves.
# En cada iteración del bucle anidado, asigna un par clave-valor 
# al diccionario sub_dict usando la clave actual de claves y el 
# valor actual de la tupla anidada.
# Agrega el diccionario sub_dict a la lista resultado.
# Una vez que el bucle for termina, imprime la lista resultante 
# resultado de diccionarios como una cadena con un mensaje.

# inicializamos tupla 
tupla_prueba = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

# inicializamos claves 
claves = ['clave', 'valor', 'id']

# inicializamos el diccionario de resultados
resultado = []

# iteramos sobre la tupla y construimos el diccionario
for sub in tupla_prueba:
    sub_dict = {}
    for i in range(len(claves)):
        sub_dict[claves[i]] = sub[i]
    resultado.append(sub_dict)

# imprimimos el resultado 
print("El diccionario convertido: " + str(resultado))