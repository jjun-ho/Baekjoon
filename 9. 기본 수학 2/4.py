#1929

M ,N = map(int, input().split())
num = []
remove = []
for i in range(M, N+1):
    num.append(i)
for i in range(M,N+1):
    if i == 1:
        remove.append(i)
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            remove.append(i)
            break
for i in remove:
    num.remove(i)

for i in num:
    print(i)