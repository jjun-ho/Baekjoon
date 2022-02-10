num =[]
for i in range(9):
    l = int(input())
    num.append(l)

max = num[0]
for i in range(8):
    if max < num[i+1]:
        max = num[i+1]

print(max)
print(num.index(max)+1)