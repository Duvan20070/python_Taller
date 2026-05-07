class GestorPacientes:
    def __init__(self):
        self.lista_pacientes = []

    def agregar_paciente(self, persona):
        self.lista_pacientes.append(persona)

    def buscar_paciente(self, apellido):
        for paciente in self.lista_pacientes:
            if paciente.apellido.lower() == apellido.lower():
                return paciente
        return None

    def actualizar_datos(self, apellido, nuevo_peso, nueva_altura):
        paciente = self.buscar_paciente(apellido)

        if paciente:
            paciente.peso = nuevo_peso
            paciente.altura = nueva_altura
            return True

        return False