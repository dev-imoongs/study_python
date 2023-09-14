
class Calculation:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return print(self.result)

    def subtract(self, num):
        self.result -= num
        return print(self.result)

    def multiply(self, num):
        self.result *= num
        return print(self.result)

    def divide(self, num):
        if num != 0:
            self.result /= num
            return print(self.result)
        else:
            print("0으로는 나눌수 없습니다.")


my_calculator = Calculation()

my_calculator.__init__() # 초기화 버튼
my_calculator.add(15)
my_calculator.subtract(3)
my_calculator.multiply(3)
my_calculator.divide(9)

print("결과값:", my_calculator.result)

