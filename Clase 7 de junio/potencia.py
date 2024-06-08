# Función recursiva para averiguar la potencia de un número.
# N^P.

def potencia(N, P):
 
    # Si la potencia es 0, devuelve 1
    if P == 0:
        return 1
    # recursividad
    return (N * potencia(N, P-1))
 
 

if __name__ == '__main__':
    N = 5
    P = 4
 
    print(potencia(N, P))