from Logica.entidades import Medico, Cita
from Logica.gestor_clinica import GestorClinica

class ConsolaVista:
    def __init__(self,):
        self.gestor = GestorClinica()

    def registrar_cita(self):
        print("\n---Registrar Cita---")


        nombre_paciente = input("Nombre del paciente: ")
        id_paciente = input("ID del paciente: ")

        paciente = self.gestor.obtener_o_crear_pacientes(nombre_paciente, id_paciente)

        nombre_medico = input("Nombre del medico: ")
        especialidad = input("Especialidad: ")
        id_medico = input("ID medico: ")


        medico = Medico(nombre_medico, especialidad, id_medico)

        fecha = input("Fecha (YYYY-MM-DD): ")
        hora = input( "Hora (HH:MM): ")

        cita = Cita(fecha, hora, medico)

        exito, mensaje = self.gestor.programar_cita(id_paciente, cita)

        print(mensaje)

    def mostrar_agenda(self):
        print("\n---CONSULTAR AGENDA---")

        id_paciente = input("Ingrese ID del paciente: ")

        citas = self.gestor.obtener_citas_paciente(id_paciente)

        if citas is None:
            print("El paciente no tiene citas")
            return
        
        for i, cita in enumerate(citas, 1):
            medico = cita.objeto_medico
            print(f"\nCita {i}:")
            print(f"Fecha: {cita.fecha}")
            print(f"Hora: {cita.hora}")
            print(f"Médico: {medico.nombre_medico}")
            print(f"Especialidad: {medico.especialidad}")
        