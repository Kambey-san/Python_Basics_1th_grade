import random
print(random)
from random import randint
from itertools import cycle

print('\n Цикл:')
#lst = [10, 12.5, 'str', False] - по условию ДЗ
lst = [randint(0, 10) for i in range(3)]
iterator = cycle(lst)
for i in range(len(lst) * 3):
    print(next(iterator), end=' ')