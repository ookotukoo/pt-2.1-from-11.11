# Функции высшего порядка
from functools import reduce

a = [4, 32, -10, 1, 72, 12]

# a = sorted(a, key=lambda x: x % 2 == 0)

# a = filter(lambda x: str(x)[-1] == '2', a)
a = filter(lambda x: x % 10 == 2, a)
# отфильтровать все числа, заканчивающиеся на 2


# print(*a)

list_of_stop_words = ["в", "и", "по", "за", "на"]

string_to_process = ("Сервис по поиску работы и сотрудников "
                     "HeadHunter опубликовал подборку"
                     " высокооплачиваемых вакансий в России за ноябрь 2024 года"
                     "в Москве. На первых строчках IT-архитекторы и техлиды  ")

res = filter(lambda x: not x in list_of_stop_words, string_to_process.split())

# print(*res)

# reduce



a = [1, 2, 3, 4, 5]

from functools import reduce

res = reduce(lambda x, y: x * y, a, 1)

print(res)
