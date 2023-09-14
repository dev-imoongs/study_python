class Num1:
    def __init__(self, number):
        self.number = number

class Num2:
    def __init__(self, count):
        self.count = count

    def plus(self, result):
        result += self.count
        return result

num1 = Num1(4)
print(num1.number)
num2 = Num2(7)
print(num2.count)
print(num2.plus(num1.number))