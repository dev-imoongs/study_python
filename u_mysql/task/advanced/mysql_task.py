from u_mysql.crud import *

# 학부모 회원가입
# 아이가 있다면 아이의 정보까지 입력
'''parent 테이블에 추가하는 형식으로'''
#
# parent_name = str(input("학부모 이름: "))
# parent_age = str(input("학부모 나이: "))
# parent_address = str(input("학부모 주소: "))
# parent_phone = str(input("학부모 핸드폰: "))
# parent_gender = str(input("학부모 성별: "))
# parent_type = str(input("관리자입니까?: [y/N]"))
# child_name = str(input("아이 이름: "))
# child_age = str(input("아이 나이: "))
# child_gender = str(input("아이 성별: "))
# parent_id = str(input("학부모 번호: "))
#
# parent_insert_query = "insert into tbl_parent(parent_name, parent_age, parent_address,parent_phone, parent_gender, parent_type)" \
#                     "values(%s, %s, %s, %s, %s, %s)"
# parent_insert_param = [parent_name,parent_age,parent_address,parent_phone,parent_gender,parent_type]
# save(parent_insert_query,parent_insert_param)
#
# if child_name:
#     child_insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id)" \
#                    "values(%s, %s, %s, %s)"
#     child_insert_param = [child_name, child_age, child_gender, parent_id]
#     save(child_insert_query,child_insert_param)

# 로그인(학부모 이름, 학부모 휴대폰 번호)
# 로그인된 학부모의 아이 정보 출력
# input_name = str(input("로그인 이름: "))
# input_phone = str(input("로그인 휴대폰 번호: "))
#
# login_query = "select * from tbl_parent where parent_name = %s and parent_phone = %s"
# login_param = [input_name,input_phone]
# row = find_all_param(login_query, login_param)
# if row:
#     print(f"{input_name}으로 로그인 성공!")
# else:
#     print("로그인 실패!")
#
# child_query = "select * from tbl_child c " \
#              "where c.parent_id = (select id from tbl_parent where parent_name = %s and parent_phone = %s);"
#
# child_info = find_all_param(child_query, login_param)
# print(child_info)

'''join 쓰는 방식'''
# login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
# parent_name = input("학부모 이름: ")
# parent_phone = input("학부모 핸드폰 번호: ")
#
# parent_id = login(login_query, [parent_name, parent_phone])
# print(parent_id)
# print(parent_id['id'])
# if parent_id:
#     # 로그인된 학부모의 아이 정보 출력
#     select_query = "select child_name, child_age, child_gender from tbl_parent p join tbl_child c " \
#                     "where c.parent_id = %s "
#
#     row = find_by_id(select_query, parent_id['id'])
#
#     print(row)
#
# else:
#     print('로그인 해주세요.')
# 아이의 정보 중 나이를 수정하기(아이 고유 번호를 이용)
# child_name = str(input("아이 이름: "))
# changed_age = str(input("수정할 나이: "))
# find_query = "select id from tbl_child where child_name = %s"
# row = find_one_param(find_query, child_name)
#
# update_query = "update tbl_child set child_age = %s where id = %s;"
# update_params = [changed_age, row.get('id')]
# update(update_query, update_params)

# 새로운 아이 정보 추가
# child_insert_query = "insert into tbl_child(child_name, child_age, child_gender, parent_id)" \
#                    "values(%s, %s, %s, %s)"
#     child_insert_param = [child_name, child_age, child_gender, parent_id]
#     save(child_insert_query,child_insert_param)

# 인가(Authorization): 권한 부여

# 체험학습(관리자만 가능) (부모중에 관리자가 있다고 가정하에) (parent table에 parent_type add)
# input_name = str(input("로그인 이름: "))
# input_phone = str(input("로그인 휴대폰 번호: "))
#
# login_query = "select parent_type from tbl_parent where parent_name = %s and parent_phone = %s"
# login_param = [input_name,input_phone]
# row = find_one_param(login_query, login_param)
#
#
#
# if row['parent_type'] == 'y':
#     input_title = str(input("체험학습 제목 입력: "))
#     input_content = str(input("체험학습 내용 입력: "))
#     input_trip_number = str(input("체험학습 번호 입력: "))
#     field_insert_query = "insert into tbl_field_trip(field_trip_title, field_tirp_content, field_trip_number)" \
#                         "values(%s, %s, %s)"
#     field_insert_param = [input_title, input_content, input_trip_number]
#     save(field_insert_query, field_insert_param)
# else:
#     print("관리자가 아닙니다.")

# 지원하기

# 학부모 로그인
input_name = str(input("로그인 이름: "))
input_phone = str(input("로그인 휴대폰 번호: "))
#이름과 번호로 로그인 하여 학부모의 id를 dict형태로 반환 (parent_id)
login_query = "select id from tbl_parent where parent_name = %s and parent_phone = %s"
login_param = [input_name,input_phone]
parent_id = find_one_param(login_query, login_param)

input_child_name = input("체험 학습에 갈 아이 이름을 입력하세요")

# 체험학습 고르기
# 체험학습 제목 별 id 조회
find_all_query = "select id, field_trip_title from tbl_field_trip"
row_temp = find_all(find_all_query)
print(row_temp)
input_choice = int(input("체험 학습 번호 고르기: "))

# login에서 반환한 parent_id랑 child table의 id가 같고 입력한 이름과 같으면 child 테이블의 id를 반환(child_id)
child_id_query = "select id from tbl_child c where c.parent_id = %s and c.child_name = %s"
child_id_param = [parent_id.get('id'), input_child_name]
child_id = find_one_param(child_id_query, child_id_param)

# apply 테이블에 입력 쿼리
insert_apply_query = "insert into tbl_apply(child_id, field_trip_id) " \
                     "values(%s, %s)"
insert_apply_param = [child_id.get('id'), input_choice]

# 지원
save(insert_apply_query, insert_apply_param)

#######################################################################################

