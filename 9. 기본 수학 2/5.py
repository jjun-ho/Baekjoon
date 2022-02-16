#4948

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#제한된 범위 속 소수. for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if isPrime(i):						#isPrime함수에 해당하면
        memo.append(i)					#리스트에 추가

while True:
    n = int(input())
    count = 0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
