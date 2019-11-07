import sys
script_name, time = sys.argv

pay = int(input("Введите заработную плату в час: "))
pr = int(input("Введите размер премии: "))
payment = (int(time) * pay) + pr
print(f'Размер заработной платы составил: {payment}')