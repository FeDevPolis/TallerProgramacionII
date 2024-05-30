# Crea un programa que permita a un usuario llevar un registro de tareas pendientes. 
# El programa debe:
# Permitir al usuario agregar tareas.
# Marcar tareas como completadas. agregámdole un tilde o algo que identifique 
# que se completó al principio de la tarea.
# Listar las tareas pendientes.
# Utilizar una lista y funciones separadas para gestionar las tareas.


# Definimos la lista global de tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f'Tarea "{tarea}" agregada.')

# Función para marcar una tarea como completada
def completar_tarea(tarea):
    if tarea in tareas:
        tareas[tareas.index(tarea)] = "✔ " + tarea
        print(f'Tarea "{tarea}" completada.')
    else:
        print(f'Tarea "{tarea}" no encontrada.')

# Función para listar las tareas pendientes
def listar_tareas():
    if tareas:
        print("Lista de tareas:")
        for tarea in tareas:
            print(f'- {tarea}')
    else:
        print("No hay tareas pendientes.")

# Función principal para interactuar con el usuario
def main():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Completar tarea")
        print("3. Listar tareas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            tarea = input("Ingresa la descripción de la tarea: ")
            agregar_tarea(tarea)
        elif opcion == '2':
            tarea = input("Ingresa la descripción de la tarea a completar: ")
            completar_tarea(tarea)
        elif opcion == '3':
            listar_tareas()
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, por favor elige una opción válida.")

#if __name__ == "__main__":
main()