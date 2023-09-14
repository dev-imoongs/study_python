
# try:
#     int(input("정수를 입력하지 않는다면 너의 컴퓨터는 해킹당할 것이다.\n정수: "))
#
# except Exception as e:
#     print(e)
#     print("해킹 완료")
#
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
#
# # print(10 / 0)
# print("반드시 실행되어야 하는 문장")

# try:
#     number = int(input("10을 나누는 수(분모)를 입력하세요\n"))
#     print(10 / number)
#
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
#
# finally:
#     print("반드시 실행되어야 하는 문장")

#
# class BadWordError(Exception):
#     def __str__(self):
#         return "으응~~~ 안돼요~!"
#
#
# def check_bad_word(message):
#     if message.__contains__('바보'):
#         raise BadWordError
#
#
# message = input("채팅: ")
# check_bad_word(message)
# print(message)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 캐릭터 닉네임 정할 때 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여 발생 시 안내 메세지까지 출력하기

class BadWordError(Exception):
    def __str__(self):
        return "올바르지 않은 단어가 포함되어 있습니다."

def check_bad_word(nickname):
    for i in badword:
        if nickname.__contains__(i):
            raise BadWordError


nickname = input("닉네임: ")
badword = ['바보','멍게','해삼','운영자']

try:
    check_bad_word(nickname)
    print('생성 성공!')
except BadWordError as e:
    print(e)


