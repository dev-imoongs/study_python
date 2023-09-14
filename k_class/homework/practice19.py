#마켓 예제 dict로 변경해보았습니다.

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