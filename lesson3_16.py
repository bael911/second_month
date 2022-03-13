# class Balance:
#     def __init__(self, num):
#         self.num = num
#
#     def __str__(self, ):
#        return f'{self.num }'
#
#     def __add__(self, other):
#         print('magic metod __add__')
#         self.num = self.num + other
#         return self.num
#
#     def __sub__(self, other):
#         print('magic metod __sub__')
#         self.num -= other
#         return self.num
#
#     def __mul__(self, other):
#         print('magic metod __mul__')
#         self.num *= other
#         return self.num
#
#     def __floordiv__(self, other):
#         previous_num = self.num
#         self.num //= other
#         return f'{previous_num}// {other} = {self.num}'
#
#
# jack_balance = Balance(5000)
# vito_balance = Balance(1000)
# print(jack_balance)


# print(jack_balance + 40)
# print(jack_balance - 1)
# print(vito_balance)
# print(jack_balance.num)
#
#
# class Builder:
#     def can_build(self):
#         print('I can build !')
#
# class Doctor:
#     def can_help(self):
#         print('i can help !')
#
# class Programmer :
#     def can_write_code(self):
#         print('I can write code Python !')
#     def can_build(self):
#         print('I am a programmer !')
#
# class Person(Builder, Doctor, Programmer):
#     pass
# jack = Person()
# jack.can_build()
# class Father(Builder):
#     pass
# class Morher(Doctor):
#     pass
# class Kairat(Father,Morher):
#     pass
#

# print(Person.mro())


class Dino:
    def __init__(self, dino_name):
        self.dino_name = dino_name










