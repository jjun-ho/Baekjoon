#11653

a = int(input())
num = []
i = 1
while i < a:
    i += 1
    if a % i == 0:
        num.append(i)
        a = a/i
        i = 1
for i in num:
    print(i)