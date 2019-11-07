def fibo_gen(n):
    el = 1
    fact = 1
    for el in range(n+1):
        yield fact
        el = el + 1
        fact = fact * el


for el in fibo_gen(15):
    print(el)

