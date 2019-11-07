my_list = [int(i) for i in input("Введите список с повторяющимися элементами: ").split()]
print(my_list)
for i in my_list:
   if my_list.count(i) == 1:
       print(i)