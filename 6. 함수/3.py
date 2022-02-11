#1065

n = int(input())
count = 0
for i in range(1,(n+1)):
    num = list(map(int,str(i)))
    if i < 100:
        count+=1
    elif num[0]-num[1] == num[1]-num[2]:
        count+=1 #1000 한수 x
print(count)


