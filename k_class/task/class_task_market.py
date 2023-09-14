# 마켓은 손님 한 명에게 한 개의 상품을 판매한다.
#손님마다 할인율이 다르다
# 마켈이서 판매 시 각 손님의 할인율을 적용하여 판매한다.
#

class Market:

    def __init__(self, **menu):
        self.name = menu['name']
        self.price = menu['price']
        self.count = menu['count']
    # 상품명, 상품가격, 상품재고

    def sale_goods(self, customer):
        self.count -= 1
        discounted_fee = self.price * (1 - customer.discount)
        print(f"{self.name}의 원가{self.price}원, 개인 할인율{customer.discount*100}% 적용하여")
        return discounted_fee

class Customer:

    def __init__(self, **info):
        self.user_name = info['user_name']
        self.age = info['age']
        self.discount = info['discount']
    # 이름, 나이, 할인율




menu = [{'name':'과자','price': 4000,'count': 10},
        {'name':'아이스크림','price': 2000 ,'count': 5},
        {'name':'음료수','price': 1000 ,'count': 15}]

info = [{'user_name':'홍길동','age': 40 ,'discount': 0.2},
        {'user_name':'김대한','age': 20,'discount': 0.10},
        {'user_name':'이민국','age': 18,'discount': 0.05}]

customer1 = Customer(**info[0])
customer2 = Customer(**info[1])
customer3 = Customer(**info[2])
menu1 = Market(**menu[0])
menu2 = Market(**menu[1])
menu3 = Market(**menu[2])
print(menu1.sale_goods(customer1))
print(menu2.sale_goods(customer3))
#

# 마켓은 손님 한 명에게 한 개의 상품을 판매한다.
# 손님마다 할인율이 다르다
# 마켓에서 판매 시 손님의 할인율을 적용하여 판매한다.

# #######################강사님 풀이#########################
# class Market:
#     # 상품명, 상품가격, 상품 재고
#     def __init__(self, name, price, stock=0):
#         self.name = name
#         self.price = price
#         self.stock = stock
#
#     def sell(self, customer):
#         discount_price = self.price - (self.price * customer.discount * 0.01)
#         customer.money -= int(discount_price)
#         self.stock -= 1
#
#
# class Customer:
#     # 이름, 나이, 할인율(10%)
#     def __init__(self, name, age, discount, money):
#         self.name = name
#         self.age = age
#         self.discount = discount
#         self.money = money
#
#
# customer = Customer('한동석', 20, 30, 40000)
# market = Market('감자', 1500, 50)
#
# market.sell(customer)
# print(customer.money)