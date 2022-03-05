#2751

import sys
n = int(input())
number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))
number.sort()
for i in number:
    print(i)

"""
시간 초과를 막기 위해 import sys를 한 뒤, input() 대신 sys.stdin.readline()을 사용하였다.
"""