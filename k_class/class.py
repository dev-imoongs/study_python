# static
class A:
    data = 10

# a = A()
# A.data = 20
# print(A.data)

class A:
    # 생성자
    def __init__(self, data, name):
        self.data = data
        self.name = name

a = A(10,'임웅빈')
print(a.name)
print(a.data)