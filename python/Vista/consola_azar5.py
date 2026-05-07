from Logica.azar_modelos5 import Jugador, Dado, Tablero


class ConsolaAzar:
    def __init__(self):
        self.tablero = Tablero()
        self.dado = Dado()
        self.jugadores = []

    def registrar_jugadores(self):
        cantidad = int(input("¿Cuántos jugadores participan?: "))

        for i in range(cantidad):
            nombre = input(f"Nombre del jugador {i + 1}: ")
            self.jugadores.append(Jugador(nombre))

    def mostrar_tablero(self):
        print("\nTablero:")

        for i in range(5):
            valor = self.tablero.huecos[i]

            if valor is None:
                print(f"Hueco {i + 1}: vacío")
            else:
                print(f"Hueco {i + 1}: {valor}")

        print("Hueco 6: pozo")

    def mostrar_fichas(self):
        print("\nFichas de jugadores:")

        for jugador in self.jugadores:
            print(f"{jugador.nombre}: {jugador.fichas}")

    def jugar(self):
        self.registrar_jugadores()

        while True:
            for jugador in self.jugadores:
                if jugador.sin_fichas():
                    continue

                input(f"\nTurno de {jugador.nombre}. Presiona Enter para lanzar el dado...")

                numero = self.dado.lanzar()
                print(f"{jugador.nombre} lanzó: {numero}")

                resultado = self.tablero.jugar_turno(jugador, numero)

                if resultado == "pozo":
                    print("La ficha cayó en el pozo y salió del juego.")
                elif resultado == "ocupa":
                    print(f"{jugador.nombre} ocupó el hueco {numero}.")
                elif resultado == "limpia":
                    print(f"{jugador.nombre} recogió la ficha del hueco {numero}.")
                elif resultado == "sin_fichas":
                    print(f"{jugador.nombre} ya no tiene fichas.")

                self.mostrar_tablero()
                self.mostrar_fichas()

                if jugador.sin_fichas():
                    print(f"\n{jugador.nombre} ganó la partida.")
                    return