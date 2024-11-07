class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de instancia
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Método de clase
    @classmethod
    def mostrar_especie(cls):
        print(f"Especie: {cls.especie}")

    # Método estático
    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18
