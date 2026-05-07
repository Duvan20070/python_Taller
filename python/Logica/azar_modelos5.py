import random


class Jugador:
    def __init__(self, nombre, fichas=10):
        self.nombre = nombre
        self.fichas = fichas

    def quitar_ficha(self):
        if self.fichas > 0:
            self.fichas -= 1

    def agregar_ficha(self, cantidad=1):
        self.fichas += cantidad

    def sin_fichas(self):
        return self.fichas == 0


class Dado:
    def lanzar(self):
        return random.randint(1, 6)


class Tablero:
    def __init__(self):
        self.huecos = [None, None, None, None, None]

    def jugar_turno(self, jugador, numero):
        if jugador.fichas == 0:
            return "sin_fichas"

        jugador.quitar_ficha()

        if numero == 6:
            return "pozo"

        indice = numero - 1

        if self.huecos[indice] is None:
            self.huecos[indice] = jugador.nombre
            return "ocupa"

        jugador.agregar_ficha()
        self.huecos[indice] = None
        return "limpia"