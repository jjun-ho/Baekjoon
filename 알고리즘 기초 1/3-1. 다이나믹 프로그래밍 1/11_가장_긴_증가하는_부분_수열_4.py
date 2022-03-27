#14002

N = int(input())
input_array = list(map(int, input().split()))
dp = [1] * N  # 최장수열 길이를 저장할 dp 리스트선언

for i in range(N):  # 배열 길이만큼돈다.
    for j in range(i):  # 해당 배열 원소의 직전 원소까지 돈다.
        if input_array[i] > input_array[j]:  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입

print(max(dp))  # 최장길이 출력

subsequence = [] #정답수열 입력할 배열선언
order = max(dp)  # max(dp) 값을 저장
for i in range(N - 1, -1, -1):  # n-1 ~ 0
    if dp[i] == order:  # 만약 dp[i] 값이 order값과 같다면
        subsequence.append(input_array[i])  # 해당 input_array[i]값을 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

subsequence.reverse()  # 큰수부터 작은수로 뽑았기 때문에
print(*subsequence) #정답수열 출력

"""
dp에 저장 되어 있는 값을 잘 보면 해당 값들은 현재 배열에서 앞 원소들보다 몇번째로 큰 지에 대한 순서를 나타내준다.
10 20 10 30 20 50 을 입력한다면 dp에는 [1,2,1,3,2,4]가 저장 된다. 50은 4번째 30은 3번째 20은 2번째 10은 첫번째라는 것을 알 수 있다
7 1 2 8 3 을 일력 dp에는 [1,1,2,3,3] 
"""