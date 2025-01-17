# Clase base: Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Clase derivada: Auto (Herencia)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):  # Polimorfismo (sobrescritura)
        return f"Auto: {self.marca} {self.modelo}, {self.puertas} puertas"

# Clase para Conductor (Encapsulación)
class Conductor:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.__licencia = licencia  # Atributo privado

    def obtener_licencia(self):  # Método público para acceder al atributo privado
        return self.__licencia

    def cambiar_licencia(self, nueva_licencia):  # Método público para modificar el atributo privado
        if nueva_licencia:
            self.__licencia = nueva_licencia
            print("Licencia actualizada con éxito.")
        else:
            print("La licencia no puede ser vacía.")

    def __str__(self):
        return f"Conductor: {self.nombre}, Licencia: {self.__licencia}"

# Función para demostrar polimorfismo
def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion())

# Crear instancias
vehiculo = Vehiculo("Chevrolet", "Optra")
auto = Auto("Chevrolet", "Optra", 5)
conductor = Conductor("Gabriel Ocles", "1722105499")

# Demostrar funcionalidad
print("=== Información de Vehículos ===")
mostrar_descripcion(vehiculo)  # Polimorfismo
mostrar_descripcion(auto)      # Polimorfismo

print("\n=== Información del Conductor ===")
print(conductor)
conductor.cambiar_licencia("1722105499")  # Modificar licencia (Encapsulación)
print(f"Licencia actualizada: {conductor.obtener_licencia()}")
