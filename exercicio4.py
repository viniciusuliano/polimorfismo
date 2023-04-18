import math
class Forma:
    def __init__(self):
        pass

    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def area(self):
        area_quadrado = self.lado ** 2
        return area_quadrado

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def area(self):
        area_circulo = math.pi * (self.raio ** 2)
        return round(area_circulo, 2)


formas = [Quadrado(4), Circulo(5)]
for forma in formas:
    print(forma.area())
    
