from functools import reduce

def my_l(p_1, p_2):
    return p_1 * p_2


my_list = [i for i in range(100, 1001)]
print(reduce(my_l, my_list))