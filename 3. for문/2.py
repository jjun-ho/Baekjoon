#10950

test = int(input())
sum = []
for i in range(test):
    n1, n2 = map(int,input().split())
    sum.append(n1 +n2)

for i in range(test):
    print(sum[i])

