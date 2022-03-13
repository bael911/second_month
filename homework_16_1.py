class Dog:
    def __init__(self, weight, color, height, voiceText):
        self.weight = weight
        self.color = color
        self.height = height
        self.voiceText = voiceText

    def voice(self):
        print(f'voice: {self.voiceText}')

    def __str__(self):
        return f'weight: {self.weight}\n' \
               f'color: {self.color}\n' \
               f'height: {self.height}'


rex = Dog(74, 1.75, 'black', 'gaа gaf')
print('эТО СОБАКА')
print(rex)
rex.voice()
print("-" * 40)


class Cat:
    def __init__(self, weight, color, height, voiceText):
        self.weight = weight
        self.color = color
        self.height = height
        self.voiceText = voiceText

    def voice(self):
        print(f'voice: {self.voiceText}')

    def __str__(self):
        return f'weight: {self.weight}\n' \
               f'color: {self.color}\n' \
               f'height: {self.height}'


barsik = Cat(20, 1.05, 'black and white', 'mur mur')
print('Это кот')
print(barsik)
barsik.voice()
print("-" * 40)


class Cow:
    def __init__(self, weight, color, height, voiceText):
        self.weight = weight
        self.color = color
        self.height = height
        self.voiseText = voiceText

    def voise(self):
        print(f'{self.voiseText}')

    def __str__(self):
        return f'weight: {self.weight}\n' \
               f'color: {self.color}\n' \
               f'height: {self.height}'


Ashab_Tamaev = Cow(180, 'black-white', 183, 'Насвай Барма?')
print('Это Корова')
print(Ashab_Tamaev)
Ashab_Tamaev.voise()
print("-" * 40)


class Bear:
    def __init__(self, weight, color, height, voiceText):
        self.weight = weight
        self.color = color
        self.height = height
        self.voiseText = voiceText

    def voise(self):
        print(f'{self.voiseText}')

    def __str__(self):
        return f'weight: {self.weight}\n' \
               f'color: {self.color}\n' \
               f'height: {self.height}'


Vasiliy = Bear(201, 'brown', 199, 'Русские Не Сдаютьсяяяяяяяяяяяяяя!')
print('Это Медведь')
print(Vasiliy)
Vasiliy.voise()
print('-' * 40)
