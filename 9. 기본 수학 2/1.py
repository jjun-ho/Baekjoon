#1978

t = int(input())
num = list(map(int,input().split()))
count = t

for i in num:
    if i == 1:
        count -= 1
        continue
    for j in range(2,i):
        if i%j == 0:
            count -= 1
            break
print(count)

"""
* 소수 알고리즘
소수는 1과 N(자기자신)만을 약수로 가진다: 2부터 N-1까지의 수로는 나눠져서는 안된다.
"""