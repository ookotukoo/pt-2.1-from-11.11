def greet_curried(greeting):
    def greet(name):
        print(greeting + ", " + name)
    return greet

greet_hello = greet_curried("Hello") # каррирование
greet_hello("Игорь")		# Hello, Игорь 
greet_hello("Роман")	# Hello, Роман

# вызов напрямую greet_curried:
greet_curried("Hi")("Сергей")  # Hi, Сергей 

print(hash(2**10))
print(hash(3.14))
print(hash(True))
print(hash((1,2,3)))
##print(hash({1,2,3}))
# print(hash([1, 2, 3]))
print(hash("abc"))
# print(hash({'1': 1}))
print(hash({'1': 1, '2': 2}))


