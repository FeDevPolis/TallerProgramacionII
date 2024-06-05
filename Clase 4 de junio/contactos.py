# Desarrolla un programa que permita a un usuario registrar información 
# de contactos (nombre, número de teléfono y correo electrónico). 
# El programa debe almacenar estos contactos y permitir al usuario
# buscar contactos por nombre o número de teléfono. 

def agregar_contacto(agenda, nombre, telefono, correo):
    
    agenda[nombre] = {'Telefono': telefono, 'Correo': correo}

def buscar_contacto(agenda, criterio):
    
    for nombre, info in agenda.items():
        if criterio in nombre or criterio == info['Telefono']:
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info['Telefono']}")
            print(f"Correo: {info['Correo']}")

agenda = {}

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion =='1':
        
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingresa el numero de telefono: ")
        correo = input("Ingresa el correo electronico: ")
        agregar_contacto(agenda, nombre, telefono, correo)
        print("Contacto agregado.")
    elif opcion == '2':
        criterio = input("Ingresa el nombre o numero de telefono a buscar: ")
        buscar_contacto(agenda, criterio)
    elif opcion == '3':
        break

