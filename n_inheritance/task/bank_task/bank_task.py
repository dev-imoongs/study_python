# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막

class Bank:
    charge = 0.1
    users = []
    def __init__(self, name: str, account_number: str, phone: str, password: str, balance: int):
        self.name = name
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.balance = balance

    @classmethod
    def open_account(cls, name: str, account_number: str, phone: str, password: str, balance: int):
        cls.users.append(cls.__dict__)
        return cls(name, account_number, phone, password, balance)

    @staticmethod
    def check_account_number(account_number: str) -> bool:
        for i in range(len(Bank.users)):
            if Bank.users in Bank.users[i]['account'] == account_number:


        pass

    @staticmethod
    def check_phone(phone: str) -> bool:
        pass

    @
    def deposit(self, amount):
        self.balance += amount * (1 - Bank.charge)
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount * (1 + Bank.charge) >= 0:
            self.balance -= amount * (1 + Bank.charge)
            return self.balance
        else:
            print('잔액이 부족합니다.')

    def find_info(self):
        return print(f'name: {self.name}\naccount: {self.account}\nphone: {self.phone}\n'
                     f'password: {self.password}\nbalnce : {self.balance}')

class Shinhan(Bank):
    bank_name = '신한은행'

    def deposit(self, amount):
        Bank.charge /= 2
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def find_info(self):
        print(f'{self.bank_name}')
        return super().find_info()

class Kukmin(Bank):
    bank_name = '국민은행'

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        Bank.charge /= 2
        print(Bank.charge)
        return super().withdraw(amount)

    def find_info(self):
        print(f'{self.bank_name}')
        return super().find_info()

class Kakao(Bank):
    bank_name = '카카오뱅크'

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def find_info(self):
        self.balance /= 2
        print(f'{self.bank_name}')
        return super().find_info()



customer_list = [{'name' : '홍길동', 'account' : '123-1234-123456', 'phone': '000-000-0000',
                 'password': '0000', 'balance': 100000},
                 {'name': '김대한', 'account': '234-2345-234567', 'phone': '111-111-1111',
                  'password': '1111', 'balance': 200000},
                 {'name': '이민국', 'account': '345-3456-345678', 'phone': '222-222-2222',
                  'password': '2222', 'balance': 300000}
                 ]

customer1 = customer_list[0]
customer2 = customer_list[1]
customer3 = customer_list[2]

bank = Bank(**customer1)
# bank.input_info()
# # bank.find_info()
# # bank.deposit(50000)
# # bank.find_info()
# bank.withdraw(10000)
# bank.find_info()
#
# shinhan = Shinhan(**customer1)
# shinhan.deposit(50000)
# shinhan.find_info()
# #
kukmin = Kukmin(**customer1)
# kukmin.withdraw(5000)
kukmin.find_info()
# #
kakao = Kakao(**customer1)
kakao.find_info()
kukmin.find_info()