#11052

import sys
n = int(sys.stdin.readline())
price = [0]+list(map(int,sys.stdin.readline().split()))
max = [0] * (n+1)
max[1] = price[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if max[i] < max[i-j] + price[j]:
            max[i] = max[i-j] + price[j]
print(max[n])

"""
max[i] = 카드 i개 구매하는 최대 가격 , price[k] = k개가 들어있는 카드팩 가격
max[1] = price[1]
max[2] = max[1] + price[1] or max[0] + price[2]
max[3] = max[2] + price[1] or max[1] + price[2] or max[0] + price[3]
max[4] = max3] + price[1] or max[2] + price[2] or max1] + price[3] or max[0] + price[4]
점화식은 max[i] =  max[i - k] + price[k] 
"""