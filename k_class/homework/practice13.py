class Employee:
    def __init__(self, *name_list):
        self.name = list(name_list)

    def display_info(self, id):
        print(f"{id}.{self.name[id - 1]}")

    def add_info(self, new_name):
        if new_name not in self.name:
            self.name.append(new_name)
        else:
            print('이름이 이미 있음')

    def rename_info(self,  search_name, new_name):
        if search_name not in self.name:
            print('이름이 존재하지 않음')
        else:
            self.name[self.name.index(search_name)] = new_name

    def find_info(self):
        for i in range(len(self.name)):
            self.display_info(i+1)

    def del_info(self, del_name):
        if del_name in self.name:
            self.name.remove(del_name)
        else:
            print('삭제 할 이름이 이미 없음')


name_list = ['홍길동','임웅빈','김대한','이민국','박만세']
employee = Employee(*name_list)

#단일 id 조회
employee.display_info(1)
employee.display_info(2)
employee.display_info(3)
employee.display_info(4)
employee.display_info(5)
# 추가
employee.add_info('동해물과')
# 전체 조회
employee.find_info()
# 에러 확인과 삭제
employee.add_info('홍길동')
employee.del_info('홍길동')
employee.del_info('홍길동')
employee.find_info()
# 이름 수정
employee.rename_info('임웅빈','임꺽정')
employee.find_info()
