class Animal:
    def __init__(self, animal):
        self.animal = animal


class Cachorro(Animal):
    def __init__(self, animal):
        super().__init__(animal)

    def falar(self):
        return f'AuAu'


class Gato(Animal):
    def __init__(self, animal):
        super().__init__(animal)

    def falar(self):
        return f'Miau'


class Peixe(Animal):
    def __init__(self, animal):
        super().__init__(animal)

    def falar(self):
        return f'Glub Glub'


cachorro1 = Cachorro('Cachorro')
print(cachorro1.falar())

gato1 = Gato('Gato')
print(gato1.falar())

peixe1 = Peixe('Peixe')
print(peixe1.falar())
