my_el_listo = [int(i) for i in range(20, 241)]
print(my_el_listo)
my_list = [i for i in my_el_listo if i % 21 == 0 or i % 20 == 0]
print(my_list)