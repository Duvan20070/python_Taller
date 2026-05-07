class Persona:
    def __init__(self, nombre, apellido, edad, peso, altura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def obtener_estado(self):
        imc = self.calcular_imc()

        if imc < 18.5:
            return "Bajo peso"
        elif imc <= 24.9:
            return "Normal"
        elif imc <= 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"