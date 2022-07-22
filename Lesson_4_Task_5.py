import functools
print(functools)
from functools import reduce

def list_1(num_1, num_2):
    return num_1 * num_2

list_2 = [num for num in range(100, 1001, 2)]
print(f'Список:\n{list_2}\nРезультат произведения:\n{reduce(list_1, list_2)}')