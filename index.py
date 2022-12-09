number = float(input("Podaj liczbę: "))
precision = int(input("Podaj dokładność: "))


class Binary_System:
    def __init__(self, number, precision):
        self.x = number
        self.k = precision

    def binary(self):
        result = "0,"
        y = self.x
        for i in range(self.k):
            if y >= 0.5:
                result += "1"
            else:
                result += "0"
            y = y * 2
            if y >= 1:
                y = y - 1
        return result


class Ternary_System:
    def __init__(self, number, precision):
        self.x = number
        self.k = precision

    def ternary(self):
        result = "0,"
        y = self.x
        for i in range(self.k):
            if y >= (2 / 3):
                result += "2"
            elif y >= (1 / 3):
                result += "1"
            elif y >= 0:
                result += "0"
            y = y * 3
            if y >= 2:
                y = y - 2
            if y >= 1:
                y = y - 1
        return result


binary_object1 = Binary_System(number, precision)
print("Liczba w systemie binarnym wynosi: " + binary_object1.binary())

ternary_object1 = Ternary_System(number, precision)
print("Liczba w systemie trójkowym wynosi: " + ternary_object1.ternary())