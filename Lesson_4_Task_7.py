def fact_n(num):
    f_num = 1
    for i in range(num + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1
for n in fact_n(int(input('Факториал числа: '))):
    print(n)