# Фабрика функций

my_dict = {
    'func1': lambda num: num + 1,
    'func2': lambda num: num * 2,
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "division": lambda x, y: x / y,
    'error' : lambda *x: 'ошибка'
}


def action(match, dict_func):
    if match in dict_func:
        return dict_func[match]
    return dict_func['error']


plus = action('plus1', my_dict)

print(plus(5, 5))
