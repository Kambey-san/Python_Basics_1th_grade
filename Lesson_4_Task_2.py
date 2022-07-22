import random
print(random)
from random import randint

origin_list = [randint(0, 100) for i in range(0, randint(0, 10))]
result = [num for i, num in enumerate(origin_list[1:]) if num > origin_list[i]]

print(origin_list)
print(result)