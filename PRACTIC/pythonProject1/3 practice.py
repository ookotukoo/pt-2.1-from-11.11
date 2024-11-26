'''
1. Объявите класс с именем Programmer
атрибуты для данного класса считайте из файла attr.json

{
    "name": "Иван Иванов",
    "job": "Программист",
    "city": "Москва"
}
Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job. Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
'''

import json

with open('attr.json', encoding='utf-8') as attr_json:
    json_data = json.load(attr_json)

class Programmer:
    ...


# print(json_data)

for key, value in  json_data.items():
    setattr(Programmer, key, value)

p1 = Programmer()

# print(p1.__dict__)
# print(p1.job)
# print(getattr(p1, 'job'))
# print(hasattr(p1, 'job'))
# print('job' in p1.__dict__)
# print('job' in Programmer.__dict__)


'''
2. Создайте класс Soda
(для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).

В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка.
'''

class Soda:
    def __init__(self, supplement=None):
        if supplement:
            self.supplement = supplement

    def show_my_drink(self) -> str:
        if hasattr(self, 'supplement'):
            return f'Газировка и {self.supplement}'
        return f'Обычная газировка.'


# Soda1 = Soda('Колокольчик')
# print(Soda1.show_my_drink())
# Soda2 = Soda()
# print(Soda2.show_my_drink())


'''
3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий необязательный аргумент - цвет точки (локальное свойство color).
Если цвет не указывается, то он по умолчанию принимает значение black.
Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки.
Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет yellow.
'''

class Point:
    color = 'black'
    def __init__(self, x=0, y=0, color=None):
        self.x = x
        self.y = y
        if color:
            self.color = color

    def get_data(self):
        return (self.x, self.y, self.color)


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

print(p1.__dict__)
print(p2.__dict__)

pnt = 10
points = [Point((i*2)+1, (i*2)+1, 'yellow').get_data() if i == 1 else Point((i*2)+1, (i*2)+1).get_data() for i in range(pnt)]

print(points)
