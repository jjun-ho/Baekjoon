#10989

import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1
for i in range(10001): #~10000
    if num_list[i] != 0:
        for j in range(num_list[i]):  #중복된 수 여러번 출력하기 위해
            print(i)