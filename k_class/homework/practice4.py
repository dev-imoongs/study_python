class Member:
    def __init__(self,**info):
        self.name = info["name"]
        self.age = info["age"]
        self.id = info["id"]

    def get_info(self):
        return f"이름: {self.name}, 나이: {self.age}, 회원번호: {self.id}"


info = {"name": "임웅빈", "age": 28, "id": 1}
my_member = Member(**info)

print(my_member.get_info())
