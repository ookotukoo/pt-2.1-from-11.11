'''
Задание 1
Посчитать площадь квартиры, состоящей из комнат rooms. Попробуйте применить map и reduce
'''

from functools import reduce


rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

list_square = list(map(lambda x : x['length'] * x['width'], rooms))

result = reduce(lambda x, y: x + y, list_square)

# print(result)

'''
Задание 2
'''

rus_letter = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
string = '1 a1 фb2  c3 abc100 10' # в строке нет русских букв
# print(all(list(map(lambda x: x not in rus_letter, string))))

from string import punctuation

string = '1 a1 фb2  c3 abc100 10' # в строке нет знаков препинания

# print(all(map(lambda x: x not in punctuation, string)))

file_names = 'main.py run.py app.py flask.py' # все файлы с расширением *.py

# print(all(list(map(lambda x: x[-3:] == '.py', file_names.split(' ')))))

special_sim = ['\n', '\\', '\'', '\"', '\a', '\b', '\f', '\r', '\t', '\v', '\0']

cities = 'Анапа \nАнадырь \nАбакан Альметьевск' # в строкe нет спецсимволов

# print(all(map(lambda x: x not in cities, special_sim)))

quad = '10 25 49 81 100' # в строке все полные квадраты

# print(all(map(lambda x: (int(x) ** 0.5) % 1 == 0, quad.split(' '))))

'''
Задание 3
Сколько слов длины 6, начинающихся с согласной буквы, можно составить из букв Г, О, Д? 
Каждая буква может входить в слово несколько раз. 
Слова не обязательно должны быть осмысленными словами русского языка.
'''

list_letters = 'ГОД'

from itertools import product

res = product(list_letters, repeat=6)  # сочетаний элементов с повторением

cnt = 0

for i in list(res):
    if i[0] != 'О':
        cnt += 1

# print(cnt)

'''
Задача 4. 
Есть 5 человек (2 мужчины и 3 женщины), 
сколько существует способов разбить их на пары. Вывести на экран все пары.
'''

men = ['Иван', 'Сергей']
women = ['Мария', 'Анна', 'Зоя']

def pairs(list_men: list, list_women: list) -> list:
    output_list = []
    for m in list_men:
        for w in list_women:
            output_list.append((m, w))
    return output_list

pairs = pairs(men, women)

print(pairs) # ('Иван', 'Мария'), ('Иван', 'Анна'), ('Иван', 'Зоя'), ('Сергей', 'Мария'), ('Сергей', 'Анна'), ('Сергей', 'Зоя')
print(len(pairs))
# print(pairs.counter()) # 6


'''
Задача 5 
На вход программе подается список предметов в виде строк:
зонт=1000
палатка=10000
спички=22
котелок=543

С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, 
элементами которого также являются кортежи, то есть, представить список в формате:
(('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter.
Вывести на экран список оставшихся предметов (только их названия) в одну строчку через пробел 
в порядке их следования во входных данных.
'''

string_var = '''зонт=1000
палатка=10000
спички=22
котелок=543'''