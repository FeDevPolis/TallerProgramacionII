# Código para demostrar el funcionamiento de 
# Convertir tupla anidada a diccionario con claves personalizadas 
# Usando comprensión de listas + comprensión de diccionarios 

# inicializando tupla 
tupla_prueba = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

# imprimiendo la tupla original 
print("La tupla original: " + str(tupla_prueba)) 

# Convertir tupla anidada a diccionario con claves personalizadas 
# Usando comprensión de listas + comprensión de diccionarios 
resultado = [{'clave': sub[0], 'valor': sub[1], 'id': sub[2]} 
                            for sub in tupla_prueba] 

# imprimiendo el resultado 
print("El diccionario convertido: " + str(resultado))