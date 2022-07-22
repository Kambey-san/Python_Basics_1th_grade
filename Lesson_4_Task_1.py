import sys

print(sys.path)

from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Зарплата: {time * rate + bonus}')
    except ValueError:
        print('Введите 3 значения, исключая строки и/или пустые')

salary()