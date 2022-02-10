import sys

n = int(input())
count = 0
sum = 0
data = [list(sys.stdin.readline()) for i in range(n)]
for i in range(n):
    for j in data[i]:
        if (j == 'O'):
            count += 1
            sum += count
        elif (j == 'X'):
            count = 0
            sum += count
        else:
            count = 0
            sum += count
    print(sum)
    sum = 0

