import itertools
print(itertools)
from itertools import count

iterator = count(int(input('Введите целое число, с которого начнётся генерация: ')))
print('Первые десять числ от стартового включтительно: ')
for i in range(10):
    print(next(iterator), end=' ')
