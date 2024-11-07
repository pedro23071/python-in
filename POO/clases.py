class ClasePrueba :
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Método para mostrar información
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
        
    def metodo_test(self):
        print("Este es un método de prueba")
        
        
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # Atributo protegido
        self.edad = edad      # Atributo privado

    def mostrar_edad(self):
        return self.edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    
# *Clase hija que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llama al constructor de la clase padre
        self.salario = salario          # Atributo específico de Empleado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Salario: {self.salario}")
        
        
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular       # Atributo público
        self.__saldo = saldo_inicial # Atributo privado
        self._tipo_cuenta = "Ahorros"  # Atributo protegido

    # Método público para obtener el saldo
    def obtener_saldo(self):
        return self.__saldo

    # Método público para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    # Método público para retirar dinero
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    # Método para cambiar el tipo de cuenta, accesible desde la clase o subclases
    def cambiar_tipo_cuenta(self, nuevo_tipo):
        self._tipo_cuenta = nuevo_tipo
        print(f"Tipo de cuenta cambiado a: {self._tipo_cuenta}")