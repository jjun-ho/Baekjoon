#2225

n, k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)

"""
nk 1 2 3 
0| 1 1 1
1| 1 2 3
2| 1 3 6
3| 1 4 10
4| 1 5 15

n = 0 일 때, 1 
k = 1 일 때, 1
n>0. k>1 일 때, (k-1)을 하고 0~n까지의 숫자들을 더해준다

만약 n=20, k=5 라면
20을 5개로 나눈 것은 [0+(20을 4개로 나눈것)] + [1+(19를 4개로 나눈것)] + ... + [19+(1을 4개로 나눈것)] + [20+(0을 4개로 나눈것)] 일 것이다.
즉 점화식으로 표현한다면, dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1] + dp[n][k-1] 일 것이다.
<n=n-1> dp[n-1][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1] 
따라서 dp[n][k] = dp[n-1][k] + dp[n][k-1]

파이썬에서 음수 인덱스를 지정하면 뒤에서부터 접근 -> 다차원 배열에서도 똑같이 적용
위의 i=0 -> dp[0][1] = dp[-1][1] + dp[0][0] 이므로
                      -> 0
"""