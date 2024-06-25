"""
1.
A. ¿Qué es Git y para qué se utiliza?

Git es un sistema de control de versiones distribuido que se utiliza para
gestionar y hacer un seguimiento de los cambios en archivos y proyectos 
de software. Fue creado por Linus Torvalds en 2005 para el desarrollo del
kernel de Linux.

B. Describe brevemente lo que hacen los siguientes comandos de Git:

    - git init: 
        Inicializa un nuevo repositorio de Git en el directorio actual.
    - git commit:
        Guarda los cambios preparados en el historial del repositorio con
        un mensaje.
    - git add:
        Añade cambios del directorio de trabajo al área de preparación.
    - git clone: 
        Crea una copia de un repositorio remoto en tu máquina local.

C. Describe brevemente “los tres estados” y cuál sería el flujo de trabajo
básico en Git.

Los tres estados en Git:
Working Directory (Directorio de Trabajo): 
    Es donde haces modificaciones y trabajas en los archivos.
Staging Area (Área de Preparación): 
    Es donde preparas los cambios que quieres confirmar (commit),
    añadiendo archivos o modificaciones específicas.
Repository (Repositorio): 
    Es donde se guardan las instantáneas confirmadas de tu proyecto, formando
    el historial de versiones.
Flujo de trabajo básico en Git:
- Modificar archivos en el Working Directory.
- Añadir los cambios al Staging Area con git add.
- Confirmar los cambios al Repository con git commit.

2.
Define PEP 8 y describe al menos dos de sus recomendaciones.

PEP 8 es el "Python Enhancement Proposal" número 8, un documento que 
proporciona guías y mejores prácticas para escribir código en Python. Su 
objetivo principal es mejorar la legibilidad y la consistencia del código.
(describir dos de las siguientes recomendaciones)
Indentación: 
    Usar 4 espacios por nivel de indentación (no tabulaciones).
Longitud de Línea: 
    Limitar las líneas a un máximo de 79 caracteres.
Líneas en Blanco: 
    Utilizar líneas en blanco para separar funciones y clases, así como 
    bloques de código dentro de las funciones.
Importaciones:
    Colocar las importaciones en la parte superior del archivo.
    Seguir el orden: importaciones estándar de Python, importaciones de 
    terceros, importaciones locales.
Espaciado en Expresiones y Sentencias:
    Evitar espacios innecesarios en expresiones como función(a, b) en lugar 
    de función( a, b ).
Comentarios:
    Usar comentarios en línea y docstrings para explicar el propósito del 
    código.
    Mantener comentarios actualizados y relevantes.
Nombres:
    Usar nombres significativos y descriptivos para variables, funciones y 
    clases.
    Seguir convenciones como snake_case para funciones y variables, y 
    CamelCase para clases.
Uso de Comillas: 
    Consistente uso de comillas simples (' ') o dobles (" "), y docstrings 
    con triples comillas dobles (""" """").
Operadores:
    Incluir un espacio antes y después de operadores, como x = 1 + 2.

3. 
Dada la siguiente lista con enteros num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
definir una función evaluar_lista que reciba num como argumento y que imprima
en pantalla si un número es par o impar.    
"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def evaluar_lista(num):
    for numero in num:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
"""
¿Cómo modificarías el script para que la función nos devuelva sólo los números
 impares agregando sólo dos líneas de código a la función anterior? (no se 
 consideró la definición de la variable que se asume que ya estaba definida)
"""
impares = [] #la definición de la variable que se consideraba declarada
def evaluar_lista(num):
    for numero in num:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
            impares.append(numero)  # Línea añadida: Agregar a la lista de impares
    return impares  # Línea añadida: Retornar la lista de impares

"""
4.
Explicar qué sucede durante la ejecución del siguiente fragmento de código,
detallando cada uno de los recursos aplicados:

inventario = {}

num_productos = int(input("Ingresa la cantidad de productos en el inventario a cargar: "))

for _ in range(num_productos):
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
    inventario[nombre] = cantidad

    Completo paso a paso:
- Se inicializa un diccionario vacío llamado inventario.
- Función input: Se solicita al usuario que ingrese un número, que representa 
  la cantidad de productos que desea añadir al inventario.
- Conversión a Entero: El valor ingresado por el usuario se convierte a un 
  entero utilizando int(). Esto es necesario porque input() devuelve una 
  cadena de texto, y necesitamos un número entero para el bucle siguiente.
- Asignación: El valor convertido se almacena en la variable num_productos.
- Se utiliza un bucle for para iterar num_productos veces. 
- "_" se usa como la variable de iteración, lo cual es una convención para 
  indicar que el valor de la variable no se utiliza dentro del bucle.
- Se solicita al usuario que ingrese el nombre de un producto. Este valor se 
  almacena en la variable nombre.
- Se solicita al usuario que ingrese la cantidad de ese producto específico.
  El nombre del producto se incluye en el mensaje de la solicitud utilizando 
  una f-string para mayor claridad.
- El valor ingresado se convierte a un entero utilizando int() y se almacena
  en la variable cantidad.
- El nombre del producto (nombre) se utiliza como clave en el diccionario 
  inventario, y la cantidad (cantidad) se asigna como el valor correspondiente a esa clave.
- Esto añade o actualiza la entrada en el diccionario inventario con el nombre del producto y su cantidad.

    Resumido y directo:
- Diccionarios en Python: Para almacenar y gestionar los datos de los productos.
- Funciones de Entrada y Salida (input y print): Para interactuar con el usuario.
- Conversión de Tipos (int): Para convertir las entradas del usuario de cadenas 
  de texto a enteros.
- Bucles for: Para repetir un conjunto de instrucciones para cada producto que 
  el usuario desea añadir. "_" se usa como la variable de iteración, lo cual 
  es una convención para indicar que el valor de la variable no se utiliza 
  dentro del bucle.
- F-strings: Para formatear las cadenas de texto de manera dinámica y clara en
  los mensajes de solicitud de entrada.

5.
Dado el diccionario ´estudiantes´ donde las claves son los nombres de los 
estudiantes y los valores son tuplas que contienen (edad, calificación):

estudiantes = {
    "Juan": (21, 85),
    "Ana": (22, 92),
    "Luis": (20, 78),
    "Maria": (23, 88)
}

A. Imprime el nombre del estudiante con la mayor calificación.
B. Calcula la edad promedio de los estudiantes.
"""
# A.
# Opción 1
estudiantes = {
    "Juan": (21, 85),
    "Ana": (22, 92),
    "Luis": (20, 78),
    "Maria": (23, 88)
}

# Parte A: Imprimir el nombre del estudiante con la mayor calificación
estudiante_mayor_calificacion = max(estudiantes, 
                                    key=lambda nombre: estudiantes[nombre][1])
print("Estudiante con la mayor calificación:", estudiante_mayor_calificacion)

# Parte B: Calcular la edad promedio de los estudiantes
edades = [datos[0] for datos in estudiantes.values()]
edad_promedio = sum(edades) / len(edades)
print("Edad promedio de los estudiantes:", edad_promedio)

# Opción 2
estudiantes = {
    "Juan": (21, 85),
    "Ana": (22, 92),
    "Luis": (20, 78),
    "Maria": (23, 88)
}

# Inicializamos variables para almacenar el nombre del estudiante con la mayor
# calificación y la calificación más alta
nombre_mayor_calificacion = None
mayor_calificacion = -1

# Iteramos sobre el diccionario para encontrar el estudiante con la mayor 
# calificación
for nombre, (edad, calificacion) in estudiantes.items():
    if calificacion > mayor_calificacion:
        mayor_calificacion = calificacion
        nombre_mayor_calificacion = nombre

print("Estudiante con la mayor calificación:", nombre_mayor_calificacion)

# B.
# Extraer las edades de los estudiantes
edades = [datos[0] for datos in estudiantes.values()]

# Calcular la edad promedio
edad_promedio = sum(edades) / len(edades)

print("Edad promedio de los estudiantes:", edad_promedio)

"""
6.
Importando el módulo random de Python:
Generar una lista de diez números enteros aleatorios en 1 y 100. 
  Utilizar: randint
Ordenar la lista en orden descente. Utilizar: sort
Imprimir el número más bajo y el más alto utilizando los subíndices de la 
  lista ordenada.
"""

import random  # Importar el módulo random para generar números aleatorios

# Generar una lista de diez números enteros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]

# Imprimir la lista generada (opcional, para ver la lista antes de ordenar)
print("Lista generada:", numeros_aleatorios)

# Ordenar la lista en orden descendente
numeros_aleatorios.sort(reverse=True)

# Imprimir el número más alto y el más bajo utilizando los subíndices de la lista ordenada
numero_mas_alto = numeros_aleatorios[0]  # Primer elemento de la lista ordenada
numero_mas_bajo = numeros_aleatorios[-1]  # Último elemento de la lista ordenada

# Imprimir la lista ordenada en orden descendente
print("Lista ordenada en orden descendente:", numeros_aleatorios)

# Imprimir el número más alto
print("Número más alto:", numero_mas_alto)

# Imprimir el número más bajo
print("Número más bajo:", numero_mas_bajo)

"""
7. 
  A. Definir recursividad.
  
    La recursividad es una técnica de programación en la que una función se 
    llama a sí misma para resolver un problema.
    Componentes Claves
    Caso Base: La condición que detiene la recursión.
    Caso Recursivo: La parte que descompone el problema y realiza la llamada 
    recursiva.

  B. Explicar paso a paso qué sucede al invocar la siguiente función con 2 
     como argumento.

  def factorial(n):
    if n == 0:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)

    
    factorial(2) llama a factorial(1).
    factorial(1) llama a factorial(0).
    factorial(0) retorna 1.
    factorial(1) calcula 1 * 1 y retorna 1.
    factorial(2) calcula 2 * 1 y retorna 2.

    Conclusión: La llamada factorial(2) devuelve 2, que es el factorial de 2.


    
 (lo siguiente no era necesario pero está bueno saberlo) 

    
 factorial(2)
   |
   +--> factorial(1)
           |
           +--> factorial(0)
                   |
                   +--> retorna 1
           |
           +--> calcula 1 * 1 = 1, retorna 1
   |
   +--> calcula 2 * 1 = 2, retorna 2

8.
  Completar que se mostraría en pantalla al ejecutar, teniendo en cuenta que 
  cada item condiciona a los siguientes:

  notas = [40, 100, 60, 80, 50, 70, 60]

  print(len(notas))             
    # 1. Longitud de la lista
  
  print(max(notas))            
    # 2. Valor máximo en la lista
  
  print(min(notas))            
    # 3. Valor mínimo en la lista
  
  print(sum(notas))            
    # 4. Suma de todos los elementos en la lista
  
  print(sum(notas)/len(notas)) 
    # 5. Promedio de los elementos en la lista
  
  print(notas.pop())           
    # 6. Elimina y devuelve el último elemento de la lista
  
  print(notas)                 
    # 7. La lista después de eliminar el último elemento
  
  print(notas.count(60))       
    # 8. Contar cuántas veces aparece 60 en la lista
  
  print(notas.index(80))       
    # 9. Índice del primer elemento con valor 80
  
  print(notas[1] % notas[-1])  
    # 10. Módulo del segundo elemento por el último elemento de la lista 
    # actual

    7
    100
    40
    460
    65.71428571428571
    60
    [40, 100, 60, 80, 50, 70]
    1
    3
    30
"""
