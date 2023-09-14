# 파일의 단어의 빈도수 구하기
import re
# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

list_test = []
list_test2 = []
readfile = open('alice','r',encoding='utf-8')

#
# print(read_all_line)

# print(readfile.readlines())
# print(type(readfile.readlines()))
for read_all_line in readfile.readlines():
    lower_all_line = read_all_line.strip().lower()
    # if 'a' <= lower_all_line <= 'z':

    new_all_line = re.sub(r"[^a-zA-Z]", " ", lower_all_line)
    # print(new_all_line)
    print(' '.join(new_all_line.split()))
    # list_test.append(' '.join(new_all_line.split()))
    # list_test.append(new_all_line.split())
    # print(''.join(new_all_line.split()))


# print(list_test)
"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""