#11053

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

"""
첫번째 숫자부터 검사를 해 나간다.
자기 자신(보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다.
ex) 7 8 1 2 3 -> 3
"""