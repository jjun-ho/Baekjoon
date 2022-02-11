num1, num2 =input().split()

num1 = list(str(num1))
num2 = list(str(num2))
num1_re = []
num2_re = []
for i in reversed(range(len(num1))):
    num1_re.append(num1[i])
for i in reversed(range(len(num2))):
    num2_re.append(num2[i])

result1 = int("".join(num1_re))
result2 = int("".join(num2_re))

if result1 >= result2:
    print(result1)
else:
    print(result2)

 """
 * for문 거꾸로 반복 #
1. for i in range(n,0,-1) : step을 음수로 지정
2. for i in reversed(range(n)):
 """