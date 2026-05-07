from Vista.consola_vista import ConsolaVista

def main():
    vista = ConsolaVista()

    while True:
        print("\n=== SISTEMA CLÍNICO ===")
        print("1. Registrar cita")
        print("2. Ver agenda")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            vista.registrar_cita()
        elif opcion == "2":
            vista.mostrar_agenda()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()