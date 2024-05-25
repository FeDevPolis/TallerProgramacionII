#Definición de la tupla 'evento'
evento = (
    "Evento deIADES", #Nombre del evento
    "25 de mayo de 2024", #Fecha del evento
    "Buenos Aires", #Lugar del evento
    25, #Número máximo de participantes permitidos
    [] #Lista de participantes (se usará una lista dentro de la tupla)
)

#Función para registrar un participante
def registrar_participante(nombre, apellido, dni):
    if verificar_cupo():
        nombre = input("Ingrese el nombre del participante: ")
        apellido = input("Ingrese el apellido del participante: ")
        dni= input("Ingrese el número de doc5umento del participante: ")
        participante = (nombre, apellido, dni)
        evento[4].append(participante)
        print(f"Participante {nombre} {apellido} registrado exitosamente.")
    else:
        print("No hay cupo disponible para más participantes.")

#Función para verificar si hay cupo disponible
def verificar_cupo():
    return len(evento[4]) < evento[3]

#Función para listar los participantes
def listar_participantes():
    if evento[4]:
        print("Lista de participantes registrados:")
        for i, participante in enumerate(evento[4], start=1):
            print(f"{i}. {participante[0]} {participante[1]} - Documento: {participante[2]}")
    else:
        print("No hay participantes registrados.")

#Menú interactivo
def menu():
    while True:
        print("\nMenú del Evento")
        print("1. Registrar un nuevo participante")
        print("2. Verificar cupo")
        print("3. Listar participantes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_participante(nombre, apellido, dni)
        elif opcion == "2":
            if verificar_cupo():
                print("Aún hay cupo disponible.")
            else:
                print("No hay más cupo disponible.")
        elif opcion == "3":
            listar_participantes()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 4.")

#Ejecución del menú
menu()