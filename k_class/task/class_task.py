# 동물
# 이름, 나이, 성별, 음식 개수, 체력 개수
# 먹기, 산책하기

# 먹기: 음식 1개 소진
# 산책하기: 음식 1개 획득, 체력 1개 소진
class Animal:
    def __init__(self, name, age, gender, food=0, health=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.food = food
        self.health = health

    def eat(self):
        self.food -= 1
        self.health += 1

    def walk(self):
        self.food += 1
        self.health -= 1



my_dog = Animal('강아지', 6, 'male')
my_cat = Animal('고양이', 5, 'female')
my_bird = Animal('앵무새', 4, 'male')
print(my_dog.name)
