class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor: Inicializa los atributos de la persona.

        Parámetros:
        - nombre: Nombre de la persona.
        - edad: Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años.")

    def mostrar_informacion(self):
        """
        Muestra la información de la persona.
        """
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __del__(self):
        """
        Destructor: Muestra un mensaje cuando el objeto es eliminado.
        """
        print(f"Persona eliminada: {self.nombre}, {self.edad} años.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una persona
    persona1 = Persona("Sofia", 27)
    persona1.mostrar_informacion()

    # Crear otra persona
    persona2 = Persona("Steven", 32)
    persona2.mostrar_informacion()

    # Forzar la eliminación de los objetos
    del persona1
    del persona2

    print("Fin del programa.")