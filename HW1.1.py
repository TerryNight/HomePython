from sys import argv
time, pr = argv


def simple_calc():
    pay = int(input("Введите ставку в час: "))
    payment = time * pay
    return payment + pr


print(f'Размер заработной платы составил: {simple_calc()}')