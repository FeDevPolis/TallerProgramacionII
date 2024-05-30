def caracter_mas_frecuente(s):
    # Crear un diccionario para contar las apariciones de cada carácter
    contador = {}
    
    # Contar las apariciones de cada carácter
    for caracter in s:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
            
    # Encontrar el carácter con más apariciones
    max_caracter = max(contador, key=contador.get)
    max_apariciones = contador[max_caracter]
    
    return (max_caracter, max_apariciones)

# Solicitar al usuario que ingrese una palabra
cadena = input("Por favor, ingrese una palabra: ")
resultado = caracter_mas_frecuente(cadena)
print(f"El carácter que más veces aparece es '{resultado[0]}' con {resultado[1]} apariciones.")