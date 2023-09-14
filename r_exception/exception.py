# python에서는 exception을 error라고 부른다
try:
    int(input("정수를 입력하지 않는다면 너의 컴퓨터는 해킹당할 것이다.\n정수: "))

# 오전 11:08 except ValueError 부분 약 10분정도 다시 보기 클래스와 사용에 대해
except:
    print("해킹 완료")
#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("")
#
# finally: # except에서 밸류에러로 잡을수 없을때에도 finally는 실행 됨
#     print("무조건 실행되는 문장")
#
#
#     class BadWordError(Exception):
#         def __str__(self):
#             return "으응~~~ 안돼요~!"
#
#
#     def check_bad_word(message):
#         if message.__contains__('바보'):
#             raise BadWordError
#
#
#     message = input("채팅: ")
#     check_bad_word(message)
#     print(message)
