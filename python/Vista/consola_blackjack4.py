from Logica.blackjack_modelos4 import Baraja, Mano


class ConsolaBlackjack:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.mezclar()
        self.jugadores = []

    def registrar_jugadores(self):
        cantidad = int(input("¿Cuántos jugadores van a participar?: "))

        for i in range(cantidad):
            nombre = input(f"Nombre del jugador {i + 1}: ")
            self.jugadores.append({
                "nombre": nombre,
                "mano": Mano(),
                "activo": True
            })

    def mostrar_cartas(self, jugador):
        cartas = ""

        for carta in jugador["mano"].cartas:
            cartas += f"[{carta}] "

        total = jugador["mano"].calcular_total()
        print(f'{jugador["nombre"]}: {cartas}- Total: {total}')

    def turno_jugador(self, jugador):
        jugador["mano"].agregar_carta(self.baraja.dar_carta())
        jugador["mano"].agregar_carta(self.baraja.dar_carta())

        while jugador["activo"]:
            self.mostrar_cartas(jugador)

            total = jugador["mano"].calcular_total()

            if total > 21:
                print(f'{jugador["nombre"]} perdió por pasarse de 21 puntos.')
                jugador["activo"] = False
                break

            opcion = input(
                f'{jugador["nombre"]}, ¿pedir otra carta o plantarse? (p = pedir / n = plantarse): '
            ).lower()

            if opcion == "p":
                jugador["mano"].agregar_carta(self.baraja.dar_carta())
            else:
                print(
                    f'{jugador["nombre"]} se plantó con {jugador["mano"].calcular_total()} puntos.'
                )
                jugador["activo"] = False

    def mostrar_resultados(self):
        print("\n=== RESULTADOS FINALES ===")

        for jugador in self.jugadores:
            self.mostrar_cartas(jugador)

            total = jugador["mano"].calcular_total()

            if total > 21:
                print("Resultado: perdió\n")
            else:
                print("Resultado: válido\n")

    def determinar_ganador(self):
        mejores = []
        mayor_puntaje = 0

        for jugador in self.jugadores:
            total = jugador["mano"].calcular_total()

            if total <= 21:
                if total > mayor_puntaje:
                    mayor_puntaje = total
                    mejores = [jugador]
                elif total == mayor_puntaje:
                    mejores.append(jugador)

        if len(mejores) == 0:
            print("Todos los jugadores se pasaron de 21. No hay ganador.")
            return

        if len(mejores) == 1:
            print(
                f'El ganador es {mejores[0]["nombre"]} con {mayor_puntaje} puntos.'
            )
        else:
            nombres = ""

            for jugador in mejores:
                nombres += jugador["nombre"] + " "

            print(
                f'Hay empate entre: {nombres}con {mayor_puntaje} puntos.'
            )

    def jugar(self):
        self.registrar_jugadores()

        for jugador in self.jugadores:
            print(f"\n--- Turno de {jugador['nombre']} ---")
            self.turno_jugador(jugador)

        self.mostrar_resultados()
        self.determinar_ganador()