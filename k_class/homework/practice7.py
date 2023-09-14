class Bank:
    def __init__(self, id_number, balance):
        self.id_number = id_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"예금된 금액: {amount}원\n잔액: {self.balance}원")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f'인출하려는 금액보다 현재 잔액이 더 적습니다.\n인출하려는 금액: {amount}원\n현재 잔액: {self.balance}원')

vip = Bank(4,50000)
#예금
vip.deposit(55000)
#출금
vip.withdraw(110000)