# Комбинаторика в Python
import time
from itertools import *

content = "🧀🍄🍖"

# combinations, product, permutations

pizza = combinations(content, 2)  # сочетания
print(*pizza, sep='\n')

print()

pizza = permutations(content, 2)  # перестановки (6)
print(*pizza, sep='\n')

print()

pizza = product(content, repeat=2)  # сочетаний элементов с повторением
print(*pizza, sep='\n')

# colors = ['red', 'green', 'blue']
#
# for color in cycle(colors):
#     print(color)
#     time.sleep(1)

shiffre = '1234'

res = product(shiffre, repeat=5)

cnt = 0
for code in res:
    if code.count('1') == 2:
        cnt += 1

print(cnt)
