#2004

def fiveCount(n):  # 5가 몇번 나누어지는지를 구한다.
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

def twoCount(n):  # 2가 몇번 나누어지는지를 구한다.
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    # 2와 5의 개수를 nCm을 구할 때처럼 구해서 더 작은 개수를 선택한다.
    print(min(twoCount(n) - twoCount(m) - twoCount(n - m), fiveCount(n) - fiveCount(m) - fiveCount(n - m)))

"""
조합: 서로 다른 n개의 원소를 가지는 어떤 집합
nCk / C(n,k) 
팩토리얼로 구해서 문제 해결 -> 시간초
->
0이 생기는 경우는 10이 만들어지는 경우
끝자리 0의 개수 
= 주어진 수의 2가 몇번나누어지는지와 5가 몇번 나누어지는지를 구하고 2 와 5의 개수중 더 작은 개수를 선택
= 2,5의 쌍의 개수 -> 끝자리 0의 개수
8! = (8) 7 (6) 5 (4) 3 (2) 1 => 2가 나오는 횟수 7번이다
-> 8/2 = 4
-> 8/(2*2) = 2
-> 8/(2*2*2) = 1
100!
-> 100/5 = 20 (5, 10, 15, 20, 25 ... 100 : 5를 1개 이상)
-> 100/5^2 = 4 (25, 50, 75, 100: 5를 하나씩 더 가지고 있음(2개))
"""