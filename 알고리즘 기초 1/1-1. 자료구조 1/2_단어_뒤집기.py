#9093

import sys

n = int(sys.stdin.readline())
for i in range(n):
    sentence = sys.stdin.readline().split()
    for j in sentence:
        if len(j) == 1:
            print(j, end='')
        else:
            temp = list(j)    #문자열 슬라이싱 / stack 자료구조 사용가능
            for k in reversed(range(len(temp))):
                print(temp[k], end='')
        print(' ',end='')

"""
* 문자열 슬라이싱
1. for문 활용
s = "abcde"
s_reverse = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
for char in s:
    s_reverse = char + s_reverse
print(s_reverse)  # edcba

2.  파이썬에서 제공하는 reverse() 사용
s = "abcde"
print(''.join(reversed(s)))  # edcba

3.  문자열 슬라이싱
s = "abcde"
print(s[::-1])  # edcba
print(s[3:0:-1])  # dcb, 3번 인덱스부터 1번 인덱스까지 역순으로 출력
"""