#1978

t = int(input())
num = list(map(int, input().split()))
count = t
for i in num:
    if i == 1:
        count -= 1
        continue
    for j in range(2,i):  #i=2 일 때, for문 range(2,2)이므로 아무것도 안하고 넘어감
        if i%j == 0:
            count -= 1
            break
print(count)