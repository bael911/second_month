class Animal:
    def __init__(self, name, type, color, voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)


class Dog(Animal):
    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)


class Cat(Animal):
    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)


rex = Dog('Rex', 'Domestic', 'Blue', 'Gaf gaf')
rex.voice()
barcik = Cat('bar ik', 'Domestic', 'Blue', 'mur mur')
barcik.voice()


class Horse:
    def __init__(self, name, type, color, voiceText, speed, weight):
        super().__init__(name, type, color, voiceText)
        self.speed = speed
        self.weight = weight

    # def voice(self):
    #     print(f'{self.name}:{self.voiceText}')


mustang = Horse('mustang', 'Domestic', 'Brown', 'riri', 30, 250)
mustang.voice()
