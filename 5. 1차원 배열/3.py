#2577

A = int(input())
B = int(input())
C = int(input())

count =[]
sum = A*B*C
result = list(str(sum))
result2 = list(map(int,result))
for j in range(10):
    count.append(result2.count(j))
for i in count:
    print(i)