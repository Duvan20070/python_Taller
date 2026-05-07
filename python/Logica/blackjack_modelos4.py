import random


class Carta:
    def __init__(self, pinta, rango):
        self.pinta = pinta
        self.rango = rango

    def __str__(self):
        return f"{self.rango}{self.pinta}"

    def obtener_valor(self):
        if self.rango in ["J", "Q", "K"]:
            return 10
        elif self.rango == "A":
            return 11
        else:
            return int(self.rango)


class Mano:
    def __init__(self):
        self.cartas = []

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_total(self):
        total = 0
        ases = 0

        for carta in self.cartas:
            total += carta.obtener_valor()
            if carta.rango == "A":
                ases += 1

        while total > 21 and ases > 0:
            total -= 10
            ases -= 1

        return total


class Baraja:
    def __init__(self):
        pintas = ["♣", "♠", "♥", "♦"]
        rangos = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.mazo = []

        for pinta in pintas:
            for rango in rangos:
                self.mazo.append(Carta(pinta, rango))

    def mezclar(self):
        random.shuffle(self.mazo)

    def dar_carta(self):
        return self.mazo.pop()