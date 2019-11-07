from itertools import cycle
from sys import argv
script_name, el = argv


my_list = [i for i in range(9, 20, 2)]
for el in cycle(my_list):
    print(el)