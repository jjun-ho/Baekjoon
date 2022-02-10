count = int(input())
L = list(map(int, input().split()))

max = L[0]
min = L[0]
for i in range(count-1):
    if max < L[i+1]:
        max = L[i+1]
    if min > L[i+1]:
        min = L[i+1]

print(min, max)