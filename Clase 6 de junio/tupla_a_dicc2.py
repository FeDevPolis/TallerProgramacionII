# Código para demostrar el funcionamiento de 
# Convertir tupla anidada a diccionario con claves personalizadas 
# Usando zip() + comprensión de listas 

# inicializando tupla 
tupla_prueba = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)) 

# imprimiendo la tupla original 
print("La tupla original: " + str(tupla_prueba)) 

# inicializando claves 
claves = ['clave', 'valor', 'id'] 

# Convertir tupla anidada a diccionario con claves personalizadas 
# Usando zip() + comprensión de listas 
resultado = [{clave: valor for clave, valor in zip(claves, sub)} 
                        for sub in tupla_prueba] 

# imprimiendo el resultado 
print("El diccionario convertido: " + str(resultado))