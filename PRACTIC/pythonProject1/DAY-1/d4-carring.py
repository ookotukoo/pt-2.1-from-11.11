# Фабрика функций

my_dict = {
    'func1': lambda num: num + 1,
    'func2': lambda num: num * 2,
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "division": lambda x, y: x / y,
}

def action(match, dict_func):
    return dict_func[match]


plus = action('plus', my_dict)

print(plus(5,5))

