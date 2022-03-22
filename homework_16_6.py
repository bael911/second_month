def get_list() -> list:
    return list(range(0, 1000_000, 2))

class Solutin:
    def find_target(self, list, target):
        min = list.index(list[0])
        max = list.index(list[-1])

        c = 0
        while True:
            num = (min + max)//2
            if target > list[num]:
                min = num
                c += 1
            elif target < list[num]:
                max = num
                c += 1
            elif target == list[num]:
                c += 1
                print('пк угадал твое число, кол-во попыток:',c, 'ваше число -->',list[num])
                break

a = Solutin()
print(a.find_target(get_list(), 600))