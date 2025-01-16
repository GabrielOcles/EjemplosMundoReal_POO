class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.alimentado = False  # Indica si el animal ha sido alimentado

    def alimentar(self):
        """Marca al animal como alimentado."""
        self.alimentado = True
        print(f"{self.nombre} ({self.especie}) ha sido alimentado.")

    def __str__(self):
        return f"Animal: {self.nombre} - Especie: {self.especie} - Edad: {self.edad} años - {'Alimentado' if self.alimentado else 'Sin alimentar'}"


class Cuidador:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def alimentar_animal(self, animal):
        """Cuidador alimenta a un animal."""
        print(f"{self.nombre} está alimentando a {animal.nombre}.")
        animal.alimentar()

    def __str__(self):
        return f"Cuidador: {self.nombre} - ID: {self.id_empleado}"


class Habitat:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo  # Tipo de hábitat (ej. Selva, Desierto, Sabana)
        self.capacidad = capacidad  # Número máximo de animales
        self.animales = []  # Lista de animales en el hábitat

    def agregar_animal(self, animal):
        """Agrega un animal al hábitat si hay espacio."""
        if len(self.animales) < self.capacidad:
            self.animales.append(animal)
            print(f"{animal.nombre} ha sido agregado al hábitat {self.tipo}.")
        else:
            print(f"No hay espacio en el hábitat {self.tipo} para {animal.nombre}.")

    def mostrar_animales(self):
        """Muestra todos los animales en el hábitat."""
        print(f"Animales en el hábitat {self.tipo}:")
        if not self.animales:
            print("No hay animales en este hábitat.")
        else:
            for animal in self.animales:
                print(animal)

    def __str__(self):
        return f"Hábitat: {self.tipo} - Capacidad: {self.capacidad} - Animales: {len(self.animales)}/{self.capacidad}"


# Código principal
if __name__ == "__main__":
    # Crear animales
    animal1 = Animal("Simba", "León", 5)
    animal2 = Animal("Manny", "Elefante", 10)
    animal3 = Animal("Rango", "Camaleón", 3)

    # Crear cuidadores
    cuidador1 = Cuidador("Carlos", 101)
    cuidador2 = Cuidador("Laura", 102)

    # Crear hábitats
    selva = Habitat("Selva", 2)
    desierto = Habitat("Desierto", 1)

    # Agregar animales a los hábitats
    print("\n--- Agregando animales a los hábitats ---")
    selva.agregar_animal(animal1)  # León en la selva
    selva.agregar_animal(animal2)  # Elefante en la selva
    selva.agregar_animal(animal3)  # Camaleón (sin espacio en la selva)

    desierto.agregar_animal(animal3)  # Camaleón en el desierto

    # Mostrar animales en cada hábitat
    print("\n--- Estado de los hábitats ---")
    print(selva)
    selva.mostrar_animales()

    print(desierto)
    desierto.mostrar_animales()

    # Alimentar a los animales
    print("\n--- Alimentando animales ---")
    cuidador1.alimentar_animal(animal1)
    cuidador2.alimentar_animal(animal2)

    # Mostrar el estado final de los animales
    print("\n--- Estado final de los animales ---")
    print(animal1)
    print(animal2)
    print(animal3)