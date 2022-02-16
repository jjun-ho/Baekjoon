#1929

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)

"""
소수 판별 알고리즘
* 에라토스테네스의 체
에라토스테네스의 체에서는 1을 제거
--> 지워지지 앟는 수 중에 제일 작은 2를 소수로 선택한다 
--> 나머지 2의 배수를 모두 지운다 --> 지워지지 않는 수 중에 제일 작은 3을 소수로 선택한다 
--> 나머지 3의 배수를 지운다 ... 5, 7, 11, 13 등으로 반복을 한다.
제곱근까지만 약수의 여부를 검증해도 소수인지 아닌지 알 수 있는 이유는 6과 같은 수의 경우 2*3=3*2로 대칭을 이루기 때문이다.
"""