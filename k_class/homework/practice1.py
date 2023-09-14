# 남은 회원 기간
# 위치

class Member:

    def __init__(self, name, location, init_period):
        self.name = name
        self.location = location
        self.init_period = init_period

    def time_of_remain(self, use_period):
        remain_period = self.init_period - use_period
        print(f'{self.name}님의 {self.location}점 {use_period}일 사용하여 남아있는 회원 기간은 {remain_period}일 입니다.')

info = Member('임웅빈','부천', 85)
info.time_of_remain(24)