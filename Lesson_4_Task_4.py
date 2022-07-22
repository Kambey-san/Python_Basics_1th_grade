import random
print(random)
from random import randint

print(num := [randint(0, 9) for i in range(20)], [i for i in num if num.count(i) == 1], sep='\n')
a = (['Error exception! - unhashable type:list'])
my_dict = {i: 0 for i in a}
for i in a:
    my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])