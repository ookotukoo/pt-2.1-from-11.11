from json import dumps, loads
from time import asctime
f = open('log.txt', 'w', encoding='utf-8')

def logger(func):
    def wrapper(*args, **kwargs):
        dict = {
            "Имя-функции" : func.__name__,
            "Произвольные аргументы" : args,
            "Именованные аргументы": kwargs,
            "Возвращаемое значение": func(*args),
            "Время и дата вызова функции": asctime()
        }
        print(dumps(dict,ensure_ascii=False, indent=4), file=f)
        return 'сделано'
    return wrapper


@logger
def add_numbers(a, b):
    return a + b


@logger
def mul_numbers(a, b):
    return a * b



print(add_numbers(1,1))
print(mul_numbers(1,1))