#!/usr/bin/env python
# coding: utf-8

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

# In[1]:


import sys
from sys import argv


# In[ ]:


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Зарплата: {time * rate + bonus}')
    except ValueError:
        print('Введите 3 значения, исключая строки и/или пустые')

salary()


# #### 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# 

# In[2]:


import random
from random import randint


# In[4]:


origin_list = [randint(0, 100) for i in range(0, randint(0, 10))]
result = [num for i, num in enumerate(origin_list[1:]) if num > origin_list[i]]

print(origin_list)
print(result)


# #### 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# #### Подсказка: используйте функцию range() и генератор.

# In[5]:


my_list = [num for num in range(20, 241) if num % 20 == 0 or num % 21 ==0]
print(my_list)


# #### 4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.
# 

# In[6]:


import random
from random import randint


# In[9]:


print(num := [randint(0, 9) for i in range(20)], [i for i in num if num.count(i) == 1], sep='\n')
a = (['Error exception! - unhashable type:list'])
my_dict = {i: 0 for i in a}
for i in a:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])


# #### 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# #### Подсказка: использовать функцию reduce().
# 

# In[10]:


import functools
from functools import reduce


# In[12]:


def list_1(num_1, num_2):
    return num_1 * num_2

list_2 = [num for num in range(10, 101, 2)] #здесь сознательно уменьшил в 10 по сравнению с условием - бумага не терпит ;))
print(f'Список:\n{list_2}\nРезультат произведения:\n{reduce(list_1, list_2)}')


# #### 6. Реализовать два небольших скрипта:

# #### *итератор, генерирующий целые числа, начиная с указанного:

# In[13]:


import itertools
from itertools import count


# In[15]:


iterator = count(int(input('Введите целое число, с которого начнётся генерация: ')))
print('Первые десять чисел от стартового включительно: ')
for i in range(10):
    print(next(iterator), end=' ')


# #### *итератор, повторяющий элементы некоторого списка, определённого заранее:
# 

# In[16]:


import itertools
from itertools import cycle


# In[20]:


print('\n Цикл:')
lst = [10, 12.5, 'str', False]
#lst = [randint(0, 10) for i in range(3)] - если генерировать
iterator = cycle(lst)
for i in range(len(lst) * 3):
    print(next(iterator), end=' ')


# #### 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# 

# In[21]:


def fact_n(num):
    f_num = 1
    for i in range(num + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1
for n in fact_n(int(input('Факториал числа: '))):
    print(n)


# In[ ]:




