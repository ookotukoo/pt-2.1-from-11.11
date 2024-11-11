# Карринг (частный случай замыкания или зашивания)



def greet_curried(greeting):
    def greet(name):
        print(greeting + ", " + name)
    return greet


greet_hello = greet_curried("Hello")



greet_hello("Игорь")
greet_hello("Роман")

greet_curried("Привет")("Алексей")