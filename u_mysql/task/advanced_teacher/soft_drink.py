from u_mysql.crud import *
from random import randint

# 음료수 등록
# save_query = "insert into tbl_soft_drink(soft_drink_name, soft_drink_price) " \
#              "values(%s, %s)"
#
# for i in range(10):
#     save(save_query, [f'음료수{i + 1}', 3000 + i * 200])


# 상품 등록
# save_query = "insert into tbl_product(product_name) " \
#              "values(%s)"
#
# for i in range(20):
#     save(save_query, [f'상품{i + 1}'])

# 당첨 번호 등록
# get_count_product_query = "select count(id) product_count from tbl_product"
#
# find_all_query = "select id from tbl_product"
# products = find_all(find_all_query)
# products_ids = []
# for product in products:
#     products_ids.append(product.get('id'))
#
# save_query = "insert into tbl_lottery(product_id) " \
#              "values(%s)"
#
# for i in range(30):
#     index = randint(0, get_count(get_count_product_query).get('product_count') - 1)
#     random_product = products_ids[index]
#     save(save_query, random_product)


# 음료수 랜덤, 당첨번호 랜덤
get_count_soft_drink_query = "select count(id) soft_drink_count from tbl_soft_drink"
get_count_lottery_query = "select count(id) lottery_count from tbl_lottery"

find_all_soft_drink_query = "select id from tbl_soft_drink"
find_all_lottery_query = "select id from tbl_lottery"

soft_drinks = find_all(find_all_soft_drink_query)
lotteries = find_all(find_all_lottery_query)

soft_drink_ids = []
lottery_ids = []

for soft_drink in soft_drinks:
    soft_drink_ids.append(soft_drink.get('id'))

for lottery in lotteries:
    lottery_ids.append(lottery.get('id'))

save_query = "insert into tbl_circulation(soft_drink_id, lottery_id) " \
             "values(%s, %s)"

# 확률
# 단위 정하기: 10단위
rating_box = [0] * 10
rating = 30
for i in range(rating // 10):
    rating_box[i] = 1

for i in range(100):
    random_index = randint(0, 9)
    soft_drink_index = randint(0, get_count(get_count_soft_drink_query).get('soft_drink_count') - 1)
    lottery_index = randint(0, get_count(get_count_lottery_query).get('lottery_count') - 1)

    random_soft_drink = soft_drink_ids[soft_drink_index]
    random_lottery = lottery_ids[lottery_index]

    # 70% 확률
    if rating_box[random_index] == 0:
        random_lottery = None

    save(save_query, [random_soft_drink, random_lottery])
