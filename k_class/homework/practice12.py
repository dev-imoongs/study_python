
class Person:
    def __init__(self, **info):
        self.name = info['name']
        self.location = info['location']

    def introduce(self):
        print(f"안녕하세요, 저는 {self.location}에 거주하는 {self.name}입니다.")

info = [{'name': '임웅빈','location':'부천'},
        {'name': '홍길동','location':'역삼'}]

for i in range(len(info)):
    temp = i + 1
    temp = Person(**info[i])
    temp.introduce()

# 또는
# person1 = Person(**info[0])
# person2 = Person(**info[1])
# person1.introduce()
# person2.introduce()
