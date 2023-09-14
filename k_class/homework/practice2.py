# 과일 가게 재고 관리
# 사과, 바나나, 딸기, 수박
# 상품명, 가격, 재고

class Market_fruit:
    count_of_product = 0

    def __init__(self, name, price, count_of_product):
        self.name = name
        self.price = price
        self.count_of_product = count_of_product

    def sell(self, customer_name, customer_money, buy_num):
        customer_money -= self.price * buy_num
        if self.count_of_product > buy_num:
            self.count_of_product -= buy_num
            print(f'{customer_name}님이 {self.price}원의 {self.name}를 {buy_num}개 '
                  f'구매하여 잔액 {customer_money}, {self.name}의 재고는 {self.count_of_product}개 남았습니다')
        else:
            print('재고가 부족합니다')

apple = Market_fruit('사과', 2000, 5)
apple.sell('임웅빈',10000,2)
apple.sell('임웅빈',6000,1)
apple.sell('임웅빈',4000,3)
