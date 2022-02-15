#2581

M = int(input())
N = int(input())

num = []
remove = []
for i in range(M, N+1):
    num.append(i)
for i in range(M,N+1):
    if i == 1:
        remove.append(i)
        continue
    for j in range(2,i):
        if i % j == 0:
            remove.append(i)
            break
for i in remove:
    num.remove(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))

"""
* min 
min(x)은 인수로 받은 자료형 내에서 최소값을 찾아서 반환하는 함수 입니다.
여기서 중요한게 x는 iterable 한 자료형이 들어가야한다는 것 입니다.
iterable 이란 반복이 가능한 데이터 타입 즉, member를 하나씩 반환(접근)할 수 있는 데이터 타입을 말합니다. 
이런 iterable 자료형으로는 문자열, 리스트, 튜플 등이 있습니다.
"""