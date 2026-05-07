class Mascota:
    def __init__ (self, nombre, edad_cronologica):
        self.nombre = nombre
        self.edad_cronologica = edad_cronologica
    
    def calcular_edad_humana(self):
        raise NotImplementedError(
            "Las subclases deben implementar este metodo"
        )

class Gato(Mascota):
    def __init__ (self, nombre, edad_cronologica):
        super().__init__(nombre, edad_cronologica)
    
    def calcular_edad_humana(self):
        if self.edad_cronologica == 1:
            return 15
        elif self.edad_cronologica == 2:
            return 24
        elif self.edad_cronologica > 2:
            return 24
        return 0
    

class Perro(Mascota):
    def __init__ (self, nombre, edad_cronologica, tamaño):
        super().__init__(nombre, edad_cronologica)
        self.tamaño = tamaño 
    
    def calcular_edad_humana(self):
        if self.tamaño == "p":
            return self.edad_cronologica * 5
        elif self.tamaño == "m":
            return self.edad_cronologica * 6
        elif self.tamaño == "g":
            return self.edad_cronologica * 7
        else:
            return 0
        