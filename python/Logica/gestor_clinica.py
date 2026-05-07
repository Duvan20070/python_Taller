from Logica.entidades import Paciente

class GestorClinica:
    def __init__(self):
        self.diccionario_pacientes = {}

    def obtener_o_crear_pacientes(self, nombre, id_paciente):
        if id_paciente not in self.diccionario_pacientes:
            self.diccionario_pacientes[id_paciente] = Paciente(nombre, id_paciente)

            return self.diccionario_pacientes[id_paciente]
    
    def programar_cita(self, id_paciente, objeto_cita):
        paciente = self.diccionario_pacientes.get(id_paciente)

        if not Paciente:
            return False, "Paciente no encontrado"
        
        return paciente.agregar_cita(objeto_cita)

    def obtener_citas_paciente(self, id_paciente):
        paciente = self.diccionario_pacientes.get(id_paciente)

        if not Paciente:
            return None
    
        return paciente.lista_citas