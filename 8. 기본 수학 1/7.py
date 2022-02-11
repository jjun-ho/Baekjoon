#2839

num = int(input())

count1 = num // 5
count = 0
if (num % 5 == 0):
    count = count1
    print(count)

else:  # 나머지 1,2,3,4
    for i in reversed(range(count1 + 1)):
        if i == 0:
            if (num % 3 != 0):
                print(-1)
                break
            elif (num % 3 == 0):
                count = num / 3
                print(int(count))
                break
        else:
            if ((num - (5 * i)) % 3 == 0):
                count = i + (num - (5 * i)) / 3
                print(int(count))
                break

"""
* // 
// 연산자: 나머지 버리고 정수 부분만
/ 연산자: 나머지까지
% 연산자: 나머지만
"""






