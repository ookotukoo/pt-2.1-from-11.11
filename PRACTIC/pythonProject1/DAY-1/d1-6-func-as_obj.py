# Функция как тип

def say_hello():
    print("Hello")


message = say_hello


# print(id(message))
#
# message()

def do(a, b, op): # как параметр функции
    return op(a, b)


def sum(a, b): return a + b


def multiply(a, b): return a * b


def select_op(choice): # как результат функции
    return sum if choice == 1 else multiply

op2 = select_op(1)
op3 = select_op(2)

print(op2(10,20))
print(op3(10,20))


# op = sum
# op1 = multiply
#
# res = op(10, 20)
# res1 = op1(10, 20)
#
# print(res)
# print(res1)
#
# print(do(5, 5, multiply))
# print(do(5, 5, sum))
# print(do(50, 5, max))
