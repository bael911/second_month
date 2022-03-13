class Matetial:
    def __init__(self, color):
        self.color = color

    def voice(self):
        print(f'{self.color}')


class Bytylka(Matetial):
    def __init__(self, color, weight):
        super().__init__(color)
        self.weight = weight
        print(f'{self.color} {self.weight}')

class Truba(Matetial):
    def __init__(self, color):
        super().__init__(color)


Plastik = Bytylka('Black', 0.5)
Plastik.voice()
