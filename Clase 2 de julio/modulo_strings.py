#modulo_strings.py

def contar_vocales(texto):  #"hola mundo"
    vocales = 'aeiouAEIOU'
    return sum(1 for char in texto if char in vocales)

def invertir_texto(texto):
    return texto[::-1]