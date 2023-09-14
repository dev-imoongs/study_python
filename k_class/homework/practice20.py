# 메뉴 소요시간 = 메뉴 가치 * 수량
class Cafe_app:
    def __init__(self, name):
        self.name = name

    def take_time(self, **example):
        time = list(example.values())
        if self.name in example:
            total = 1
            for i in time:
                total *= i
            return total


example = {'아메리카노': 5, '수량': 2}
cafe_app = Cafe_app('아메리카노')
print(f'{cafe_app.take_time(**example)}분 소요 됩니다.')