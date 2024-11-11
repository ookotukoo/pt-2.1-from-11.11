



class int(int):
    def __add__(self, other):
        return self * other

x = int(5)

z = x + 5

print(z)
