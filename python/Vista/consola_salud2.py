from Logica.salud_imc2 import Persona
from Logica.gestion_pacientes2 import GestorPacientes


class ConsolaSalud:
    def __init__(self):
        self.gestor = GestorPacientes()

    def registrar_paciente(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))

        persona = Persona(nombre, apellido, edad, peso, altura)
        self.gestor.agregar_paciente(persona)

        print("Paciente registrado correctamente.")

    def ver_lista_pacientes(self):
        if len(self.gestor.lista_pacientes) == 0:
            print("No hay pacientes registrados.")
            return

        for paciente in self.gestor.lista_pacientes:
            print(f"\nNombre: {paciente.nombre}")
            print(f"Apellido: {paciente.apellido}")
            print(f"Peso: {paciente.peso} kg")
            print(f"Altura: {paciente.altura} m")
            print(f"IMC: {paciente.calcular_imc():.2f}")
            print(f"Estado: {paciente.obtener_estado()}")

    def actualizar_paciente(self):
        apellido = input("Apellido del paciente: ")
        paciente = self.gestor.buscar_paciente(apellido)

        if not paciente:
            print("Paciente no encontrado.")
            return

        nuevo_peso = float(input("Nuevo peso (kg): "))
        nueva_altura = float(input("Nueva altura (m): "))

        self.gestor.actualizar_datos(apellido, nuevo_peso, nueva_altura)
        print("Datos actualizados correctamente.")