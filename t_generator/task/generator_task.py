import random

# 전달받은 명 수만큼 정보를 dict로 리턴한다.
# 리턴할 정보
# 번호, 이름, 전공

names = ['김보령', '김혜빈', '임수현', '이서호', '임웅빈', '장동혁']
majors = ['컴퓨터 공학', '국문학', '기계 공학', '의료 공학', '토목 공학']

#
info_list = []
info_dict = {}
count = 5
def get_list(count: int = 0) -> dict :
    for i in range(count):
        k = names[random.choice(range(len(names)))]
        v = majors[random.choice(range(len(majors)))]
    return {k : v}
def get_generator(count: int=0) ->dict:
    pass

get_list()
print(get_list())
get_list()
print(get_list())
get_list()
print(get_list())
get_list()
print(get_list())


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

