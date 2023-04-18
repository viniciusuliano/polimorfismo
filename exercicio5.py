class Empregado:
    def __init__(self):
        pass

    def pagarSalario(self):
        pass

class EmpregadoHora(Empregado):
    def __init__(self, hora, pagar):
        super().__init__()
        self.hora = hora
        self.pagar = pagar

    def pagarSalario(self):
        salario = self.hora * self.pagar
        return salario
    
class EmpregadoMes(Empregado):
    def __init__(self, dias, pagar):
        super().__init__()
        self.dias = dias
        self.pagar = pagar

    def pagarSalario(self):
        self.dias = self.hora * 8
        salario = self.dias + self.pagar
        return salario

