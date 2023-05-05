class Animal:

    def __init__(self, pet):
        self.pet = pet

    def falar(self):
        pass


class Gato(Animal):
    def __init__(self, pet):
        super().__init__(pet)

    def falar(self):
        return f'MiAu'


class Cachorro(Animal):
    def __init__(self, pet):
        super().__init__(pet)

    def falar(self):
        return f'AuAu'


lista_animais = [Cachorro('Marvin'), Gato('Morrice')]
for animal in lista_animais:
    print(f'{animal.pet} faz {animal.falar()}')
