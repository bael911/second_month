class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


class Vito(Jack):
    def __init__(self, first_name, last_name, phone_number, balance, number):
        super().__init__(first_name, last_name, phone_number, balance)
        self.number = number

    def result(self):
        print(f'Jack balance: {Jack.balance - self.number}\n Vito balance : {Vito.balance + self.number}')


Jack = Jack('Jack', 'White', '87675', 3500)
Vito = Vito('Vito', 'Swith', '214242', 1500, 500)
Vito.result()