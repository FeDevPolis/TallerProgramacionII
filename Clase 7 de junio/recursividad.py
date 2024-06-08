# Factorial de un numero N se define como el producto de todos los números enteros desde 1
# hasta N. Ej: 3! = 3 x 2 x 1 = 6

# Recursividad es cuando una función se invoca a si misma.

def factorial(n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


#def funcioncualquiera(func):
#    funcioncualquiera(func)    
#    return 





