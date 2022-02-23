#10872

def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))

"""
* 재귀 함수 : 함수 자기 자신을 호출하는 함수를 말한다.

* for문 코드
n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)
"""