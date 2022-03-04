#2798

import sys

n, m = map(int,input().split())
data = list(map(int, sys.stdin.readline().split()))
sum = []
result = 0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum.append(data[i]+data[j]+data[k])
for i in sum:
    if i > m:
        continue
    else:
        result = max(result, i)
print(result)

"""
*  max (arg1, arg2)
응용형 : max(iterable1, iterable2, ...)
매개변수 : 반복이 가능한 자료형 '들'
반환형 : 매개변수로 들어온 반복이 가능한 인자들 중에 가장 큰 데이터를 반환합니다.
"""