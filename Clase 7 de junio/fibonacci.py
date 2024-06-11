# En matemática, la sucesión de Fibonacci se trata de una serie infinita de números naturales 
# que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los 
# dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        secuencia = fibonacci(n - 1)
        secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia

def main():
    while True:
        try:
            num = int(input("Ingrese la cantidad de números de la secuencia de Fibonacci que desea imprimir: "))
            if num <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero positivo.")
    
    fibonacci_secuencia = fibonacci(num)
    print(f"Secuencia de Fibonacci con {num} números:")
    for index, value in enumerate(fibonacci_secuencia):
        print(f"{index + 1}: {value}")

if __name__ == "__main__":
    main()