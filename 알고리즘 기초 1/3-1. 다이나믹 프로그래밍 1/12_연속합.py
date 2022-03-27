#1912

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
sum = [a[0]]  # 0번째 인덱스에는 비교를 위해 a[0] 넣어줌
for i in range(len(a) - 1):
    # sum의 i번째 인덱스와 a의 i + 1번째 인덱스의 숫자를 합한 값과 a의 i + 1번째 숫자를 비교하여 더 큰 숫자를 sum리스트에 넣어준다.
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))