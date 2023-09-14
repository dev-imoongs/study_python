class Man:
    def __init__(self, name):
        self.name = name
        self.score = []

    def add_score(self, score):
        self.score.append(score)

    def get_average_score(self):
        sum = 0
        for i in self.score:
            sum += i
        return sum / len(self.score)

class Class:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_class_average(self):
        total_average = 0
        for student in self.students:
            total_average += student.get_average_score()
        return total_average / len(self.students)

class1 = Class("1반")
student1 = Man('임웅빈')
student1.add_score(80)
student1.add_score(90)

student2 = Man('홍길동')
student2.add_score(50)
student2.add_score(70)

class1.add_student(student1)
class1.add_student(student2)

print(class1.get_class_average())
