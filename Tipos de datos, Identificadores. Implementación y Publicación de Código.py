# Programa: Gestor de Tareas Personales
# Funcionalidad: Este programa permite al usuario agregar, ver y marcar como completadas sus tareas diarias.
# Autor: Gabriel

# Lista global para almacenar las tareas
tareas = []


def agregar_tarea(tarea):
    """
    Agrega una tarea a la lista de tareas.
    :param tarea: Descripción de la tarea (str)
    """
    tareas.append({"tarea": tarea, "completada": False})
    print(f"Tarea agregada: '{tarea}'")


def mostrar_tareas():
    """
    Muestra todas las tareas pendientes y completadas.
    """
    if not tareas:
        print("No tienes tareas en la lista. ¡Disfruta tu tiempo libre!")
    else:
        print("\nTus tareas:")
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['tarea']} - {estado}")
        print()


def completar_tarea(indice):
    """
    Marca una tarea como completada.
    :param indice: Índice de la tarea a completar (int)
    """
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print(f"Tarea '{tareas[indice]['tarea']}' marcada como completada.")
    else:
        print("Índice no válido. Por favor, intenta de nuevo.")


# Función principal del programa
def menu_principal():
    print("¡Bienvenido a tu Gestor de Tareas Personales!")
    while True:
        print("\nPor favor, selecciona una opción:")
        print("1. Agregar una tarea")
        print("2. Ver todas las tareas")
        print("3. Marcar una tarea como completada")
        print("4. Salir")

        opcion = input("Introduce el número de tu elección: ")

        if opcion == "1":
            nueva_tarea = input("¿Qué tarea deseas agregar? ")
            agregar_tarea(nueva_tarea)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            mostrar_tareas()
            try:
                tarea_a_completar = int(input("Introduce el número de la tarea que completaste: ")) - 1
                completar_tarea(tarea_a_completar)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "4":
            print("¡Gracias por usar el gestor de tareas! ¡Que tengas un excelente día!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el programa
menu_principal()
