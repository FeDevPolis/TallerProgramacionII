cadena_prueba = "eSta ES una cadena DE pRUEba, repito, una cadeNA DE PrueBA"

print(cadena_prueba)


# Todas las letras mayus
print(".upper   " + cadena_prueba.upper())    


# Todas las letras minus
print(".lower   " + cadena_prueba.lower())    


# Pone mayus en el comienzo de la oracion.
print(".capitalize   " + cadena_prueba.capitalize())


# La primera de cada palabra en mayus
print(".title   " + cadena_prueba.title())

# Cuenta en cuantas palbras aparece el caracter
print(cadena_prueba.count("a"))

# Cuenta cuantas veces aparece la subcadena
print(cadena_prueba.count("una"))

# Devolucion si no esta la subcadena buscada
print(cadena_prueba.count("ZZZ"))


