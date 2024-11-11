
cities = 'Москва Питер орел Сочи' # все города с большой буквы
cities = map(lambda x: x.istitle(), cities.split())

print(cities)
print(all(cities)) # если все true
print(any(cities)) # хотя бы один true

cities = 'анапа aнадыРь Абакан Альметьевск'  # все с буквы А
cities = map(lambda x: x.capitalize(), cities.split())

print(*cities)

dig = '1 2 22 33 44 55 1.11'  # в строке все числа

dig  = map(lambda x: x.isalnum(), dig.split())

print(*dig)

print('aнаПа'.capitalize())
