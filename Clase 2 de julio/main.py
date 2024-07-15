#from modulo_strings import contar_vocales, invertir_texto
#from modulo_numeros import es_primo, suma_digitos
import modulo_strings
import modulo_numeros

def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Contar vocales en un texto")
    print("2. Invertir un texto")
    print("3. Verificar si un número es primo")
    print("4. Sumar los dígitos de un número")
#    print("5. Encontrar el máximo de una lista")
#    print("6. Convertir una lista a tupla")
#    print("7. Agregar elemento a un diccionario")
#    print("8. Buscar clave en un diccionario")
#    print("9. Dividir dos números")
    print("0. Salir")

def main():
    #hacer el codigo necesario para poder cumplir con las 
    #opciones 0 - 4 del menu.
    while True:
       mostrar_menu()
       opcion = input("Seleccione una opción: ")

       if opcion == '1':
           texto = input("Ingrese un texto: ")
           print(f"El texto tiene {modulo_strings.contar_vocales(texto)} vocales.")
       elif opcion == '2':
           texto = input("Ingrese un texto: ")
           print(f"El texto invertido es: {modulo_strings.invertir_texto(texto)}")
       elif opcion == '3':
           numero = int(input("Ingrese un número: "))
           print(f"El número {numero} {'es' if modulo_numeros.es_primo(numero) else 'no es'} primo.")
       elif opcion == '4':
           numero = int(input("Ingrese un número: "))
           print(f"La suma de los dígitos de {numero} es {modulo_numeros.suma_digitos(numero)}")
       elif opcion == '0':
           print("Saliendo...")
           break
       else:
           print("Opción no válida. Intente nuevamente.")




if __name__ == "__main__":
    main()
