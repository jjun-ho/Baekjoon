#6588

from sys import stdin
array = [True for i in range(1000001)]  # 전체 수 만큼 True의 리스트 생성
for i in range(2, 1001):  # 1001 = int(math.sqrt(1000000)) + 1, 에라토스테네스 체 -> 1000^2 = 1000000: 제곱근까지만 검증해 코드 같다.
    if array[i]:
        for k in range(i + i, 1000001, i):  #range(시작 숫자, 종료숫자, step)
            array[k] = False  # i+i부터 ~ 1000000, i의 배수 index -> False
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    for i in range(3, len(array)):  # 1,2 사용x
        if array[i] and array[n-i]:  # i+(n-i) = n
            print(n, "=", i, "+", n-i)
            break  #b-a가 가장 큰 것을 출력하기 위해 찾으면 break

"""
* 에라토스테네스의 체(소수 판별 알고리즘)
에라토스테네스의 체에서는 1을 제거
--> 지워지지 앟는 수 중에 제일 작은 2를 소수로 선택한다 
--> 나머지 2의 배수를 모두 지운다 --> 지워지지 않는 수 중에 제일 작은 3을 소수로 선택한다 
--> 나머지 3의 배수를 지운다 ... 5, 7, 11, 13 등으로 반복을 한다.
제곱근까지만 약수의 여부를 검증해도 소수인지 아닌지 알 수 있는 이유는 6과 같은 수의 경우 2*3=3*2로 대칭을 이루기 때문이다.

* 시간초가 코드
import sys
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
prime = []
for i in range(3,100001):
    if i % 2 == 0:
        continue
    else:
        if isPrime(i):
            prime.append(i)
while True:
    find = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(len(prime)):
        for j in reversed(range(len(prime))):
            if prime[i] + prime[j] == n:
                find = 1
                break
        if find == 1:
            break
    if find == 1:
        print(n, " = ", prime[i], " + ", prime[j])
    else:
        print("Goldbach's conjecture is wrong.")
"""