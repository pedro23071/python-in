from clases import ClasePrueba, Persona, Empleado, CuentaBancaria

persona = ClasePrueba("Juan", 20)
persona.mostrar_informacion()
persona.metodo_test()


persona2 = Persona("Juan", 20)
print(persona2.mostrar_edad())


empleado = Empleado("Anatest", 30, 5000)
empleado.mostrar_informacion()



cuenta = CuentaBancaria("Pedro", 100)
saldo = cuenta.obtener_saldo()
print(saldo)
cuenta.depositar(500)


from Persona import Persona
persona2 = Persona("Juan", 30)
print(persona2.es_mayor_edad(20))