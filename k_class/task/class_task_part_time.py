# # PartTimer
#
# # '모든 직원'에 공통적으로 적용되는 내용
# # - 시급
# # - 직원수
#
# # '각 직원'별로 적용되는 내용
# # - 별명
# # - 근무지(기본값: '청담동')
# # - 급여 총액(초기값: 0, 생성자로 초기화 불가능)
#
# # 직원 급여 계산
# #   '근무 시간 + 상여금'에 따른 직원 급여 계산
# #   '상여금'은 지정 하지 않으면 0 으로 처리
#
# class Parttime:
#     time_fee = 5000
#     count_employee = 0
#
#     def __init__(self, name, time, bonus, location = '청담동', total_fee = 0):
#         self.name = name
#         self.time = time
#         self.bonus = bonus
#         self.loaction = location
#         self.total_fee = total_fee
#
#     def cal(self):
#         total_fee = self.time_fee * self.time + self.bonus
#         print(f'성함:{self.name}\n총 급여:{total_fee}\n근무시간:{self.time}\n상여금:{self.bonus}')
#         Parttime.count_employee += 1
#         return total_fee
#
# employee1 = Parttime('홍길동',4,30000,'원미동')
# employee2 = Parttime('김대한',8,70000)
# employee3 = Parttime('이민국',6,50000)
# employee4 = Parttime('박만세',12,100000)
#
# employee1.cal()
# employee2.cal()
# employee3.cal()
# employee4.cal()
# employee4.cal()
# print(Parttime.count_employee)
#

######################### 강사님 풀이 ########################

# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리
class PartTimer:

    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, nickname, workspace='청담동'):
        self.nickname = nickname
        self.workspace = workspace
        self.total_wage = 0
        PartTimer.total_of_part_timers += 1

    def calculate_wage(self, hour, bonus=0):
        self.total_wage += PartTimer.pay_of_hour * hour + bonus


ryan = PartTimer('라이언')
neo = PartTimer('네어', '역삼동')

print(ryan.total_wage, ryan.nickname, ryan.workspace)
print(neo.total_wage, neo.nickname, neo.workspace)

print(PartTimer.total_of_part_timers, '명')

neo.calculate_wage(3, 15000)
print(neo.total_wage)






