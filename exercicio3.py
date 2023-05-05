class Carro:
    def __init__(self, carro):
        self.carro = carro

    def dirigir(self):
        pass


class CarroEletrico(Carro):
    def __init__(self, carro):
        super().__init__(carro)

    def dirigir(self):
        print('O carro vai começar a andar: ')
        for i in range(1, 6):
            print(f'{i} KM')
        return 'O carro eletrico é potente '


class CarroGasolina(Carro):
    def __init__(self, carro):
        super().__init__(carro)

    def dirigir(self):
        print('O carro vai começar a andar: ')
        for i in range(1, 11):
            print(f'{i} KM')
        return 'O carro a gasolina é potente, porém gasta demais'


carro_eletrico = CarroEletrico('Mercedez')
print(carro_eletrico.dirigir())


carro_gasolina = CarroGasolina('BMW')
print(carro_gasolina.dirigir())
