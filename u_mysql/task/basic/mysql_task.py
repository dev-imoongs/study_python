from crud import save, find_all, update, delete, find_one, \
    find_duplication, bring_one, change_password
from task.create_random_num import create_random_num
from q_api.sms.sms import send_sms
from q_api.email_send import email_send
from q_api.papago import from_ko_to_en
from q_api.ocr import ocr
import os
import sys
#
# lib_dir = os.path.dirname(__file__)
# print(lib_dir)
# env_config = configparser.ConfigParser()
# env_config.read('lib_dir' + '/config.ini', encoding='UTF8')

# 아이디 중복검사

search_id = str(input('중복 검사 할 ID를 입력:'))
find_name_query = "select member_id from tbl_member where member_id = %s"
find_name_params = [search_id]
judge = find_duplication(find_name_query, find_name_params)
if judge == ():
    print("사용 가능한 ID입니다.")
else:
    print("중복된 ID입니다.")

# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
'''try execept finally로 해야 비정상적인 요청시 finally에서 잘못된 페이지입니다로 다 보낼수 있는데 기능 만들고 생각해보자'''
'''회원 정보 입력'''
account = str(input("id: "))
password = str(input("비밀번호: "))
name = str(input("이름: "))
'''6자리 인증번호 발송'''
six_key = create_random_num(6)
send_sms(six_key)
'''인증번호 검사'''
check_code = input("인증번호를 입력해주세요:")
if six_key == check_code:
'''인증번호 입력 후 맞으면 save로 테이블에 추가'''
    member_insert_query = "insert tbl_member(member_id, member_password, member_name" \
                          "values(%s, %s, %s)"
    member_insert_param = [account,password,name]
    save(member_insert_query,member_insert_param)
else:
    print("인증번호가 일치하지 않습니다.")

# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사
# '''id 입력후 일치하는 행에 인증번호 생성'''

'''email 발송'''
# temp_ten_code = create_random_num(10)
# email_send(temp_ten_code)

''' 인증번호 검사 후 '''

''' 비밀번호 변경기능 기존 비밀번호가 없어도 이메일 입력 후 인증번호를 입력하면 변경 되게끔 다시하기'''
# orginal_pass = str(input('기존의 비밀번호 입력:'))
# changed_pass = str(input('바꿀 비밀번호 입력:'))
# change_password_query = "update tbl_member set member_password = %s where member_password = %s"
# change_password_param = [changed_pass, orginal_pass]
# result = change_password(change_password_query,change_password_param)

# 사용자가 입력한 문장을 영어로 번역
# temp_str = str(input('입력:'))
# result = from_ko_to_en(temp_str)
# print(result)

# 한국어와 번역된 문장을 DBMS에 저장
# save
'''테이블을 하나 만들어서 member_id(fk)로 받고 korean_text, translated_text'''
'''tbl_record_translated(member_id, korean_text, translated_text)
    record_translated_query = "insert tbl_record_translated(member_id, korean_text ,translate_text)
    values(%s, %s, %s)"
    record_translated_param = [위에서 입력받고 여기 넣을지,temp_str,result]'''
# save(쿼리,파라미터)


# 번역 내역 조회
'''제대로 입력했으면 해당 테이블 조회만 하면 됨'''
# find_all(record테이블 select 쿼리,


# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
'''업로드 기능, 파일 이름만 가져오기(문자열 추출) 이미지 내용(ocr 결과값) '''
address =
ocr(address)
'''dbms에 저장, insert query'''