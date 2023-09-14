# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError

######################################################################
import datetime

class Error(Exception):
    def __str__(self):
        return '메뉴 외의 번호를 입력하였습니다 (범위: 1~4)'

class Calculator:
    def __init__(self):
        self.num1 = int(input("첫 번째 정수: "))
        self.num2 = int(input("두 번째 정수: "))
        self.operator = int(input("연산자를 선택하세요\n1 : +\n2 : -\n3 : *\n4 : /\n"))

    def __add__(self, num1: int = 0, num2: int = 0):
        return num1 + num2

    def __sub__(self, num1: int = 0, num2: int = 0):
        return num1 - num2

    def __mul__(self, num1: int = 0, num2: int = 0):
        return num1 * num2

    def __truediv__(self, num1: int = 0, num2: int = 0):
        return num1 / num2

    def calculate(self):
        datetime_now = datetime.datetime.now()
        try:

            file = open('log.txt', 'a', encoding='utf-8')

            if self.operator == 1:
                result = self.num1 + self.num2
                file.write(f'성공! [{datetime_now} : {self.num1} + {self.num2} = {result}]\n')
                return self.__add__(self.num1, self.num2)

            elif self.operator == 2:
                result = self.num1 - self.num2
                file.write(f'성공! [{datetime_now} : {self.num1} - {self.num2} = {result}]\n')
                return self.__sub__(self.num1, self.num2)

            elif self.operator == 3:
                result = self.num1 * self.num2
                file.write(f'성공! [{datetime_now} : {self.num1} * {self.num2} = {result}]\n')
                return self.__mul__(self.num1, self.num2)

            elif self.operator == 4:
                try:
                    result = self.num1 / self.num2
                    file.write(f'성공! [{datetime_now} : {self.num1} / {self.num2} = {result}]\n')
                    return self.__truediv__(self.num1, self.num2)

                except ZeroDivisionError as e:
                    file.write(f'오류! [{datetime_now} : {e}]\n')

            else:
                raise Error


            file.close()

        except Error as e:
            file = open('log.txt', 'a', encoding='utf-8')
            file.write(f'오류! [{datetime_now} : {e}]\n')
            file.close()



calculator = Calculator()
calculator.calculate()
