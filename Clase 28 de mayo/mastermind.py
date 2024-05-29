import random

def generar_cadena(longitud):
    numeros = list(range(10))
    random.shuffle(numeros)
    return numeros[:longitud]

def contar_aciertos(cadena_secreta, intento):
    aciertos = 0
    for i in range(len(cadena_secreta)):
        if cadena_secreta[i] == intento[i]:
            aciertos += 1
    return aciertos

def jugar():
    while True:
        longitud = int(input("Dime la longitud de la cadena (de 2 a 9 cifras): "))
        if 2 <= longitud <= 9:
            break
        print("Por favor, introduce un número entre 2 y 9.")

    cadena_secreta = generar_cadena(longitud)
    cadena_secreta_str = ''.join(map(str, cadena_secreta))
    
    while True:
        intento = input(f"Intenta adivinar la cadena: ")
        if len(intento) != longitud or not intento.isdigit() or len(set(intento)) != longitud:
            print(f"El intento debe ser una cadena de {longitud} cifras distintas.")
            continue
        
        aciertos = contar_aciertos(cadena_secreta_str, intento)
        
        if aciertos == longitud:
            print(f"Con {intento} has adivinado {aciertos} valores. ¡Felicidades!")
            break
        else:
            print(f"Con {intento} has adivinado {aciertos} valores. Intenta adivinar de nuevo.")
            
if __name__ == "__main__":
    jugar()