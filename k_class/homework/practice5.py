class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("멍")

class Cat(Animal):
    def make_sound(self):
        print("야옹")

dog = Dog("뽀삐")
dog.make_sound()

cat = Cat("나비")
cat.make_sound()
