class User:
    def __init__(self, nart):
        self.nart = (int(nart))
        self.pontos = 0

    def calculoPontuacao(self):
        return ''


class Autor(User):
    def __init__(self, nart):
        super().__init__(nart)

    def calculoPontuacao(self):
        return self.nart * 10 + 20


class Editor(User):
    def __init__(self, nart):
        super().__init__(nart)

    def calculoPontuacao(self):
        return self.nart * 6 + 15


autor1 = Autor(10)
print(autor1.calculoPontuacao())

editor1 = Editor(15)
print(editor1.calculoPontuacao())
