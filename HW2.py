from random import randint
my_crazy_list = [randint(10, 20) for i in range(10)]
print(my_crazy_list)
for i in range(1, len(my_crazy_list)):
    if my_crazy_list[i] > my_crazy_list[i - 1]:
        print(my_crazy_list[i])