#1989

다시 하기
t = int(input())
num = list(map(int, input().split()))
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