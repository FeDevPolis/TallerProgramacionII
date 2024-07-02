#modulo_numeros.py

def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
              
    return True

def suma_digito(numero):
    return sum(int(digito) for digito in str(numero))