class Student:
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

student = Student('임웅빈')
student.add_score(50)
student.add_score(60)
student.add_score(70)
print(student.get_average_score())