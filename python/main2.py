from Vista.consola_salud2 import ConsolaSalud


def main():
    consola = ConsolaSalud()

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE SALUD ===")
        print("1. Registrar paciente")
        print("2. Ver lista de pacientes")
        print("3. Actualizar peso/altura")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consola.registrar_paciente()
        elif opcion == "2":
            consola.ver_lista_pacientes()
        elif opcion == "3":
            consola.actualizar_paciente()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()