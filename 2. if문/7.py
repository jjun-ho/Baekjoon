#2480

case = list(map(int, input().split()))
case.sort()
count = 1
result = case[0]
sum = 0
for i in range(2):
    if case.count(case[i+1]) >= case.count(case[i]):
        count = case.count(case[i+1])
        if case[i+1] > case[i]:
            result = case[i+1]
if count == 3:
    sum = 10000 + (result)*1000
elif count == 2:
    sum = 1000 + (result)*100
elif count == 1:
    sum = (result)*100

print(sum)

"""
* count 특정 문자의 개수
문자열 안에서 찾고 싶은 문자(숫자)의 개수를 찾을 수 있다.
어떤 함수는 문자열에서만 사용 가능한 함수도 있는데 count 함수는 튜플, 리스트, 집합과 같은 반복 가능한 iterable 자료형에서도 사용 가능하다

* sort 리스트 정렬함수
list.sort() 메서드는 list 객체 자체를 정렬해주는 함수입니다. 리스트에만 사용이 가능합니다. list 객체의 멤버 함수, 즉 메서드입니다.
list.sort() 함수는 기본적으로 리스트를 오름차순으로 정렬해주는 기능을 합니다.
새로운 정렬된 리스트를 반환하는 함수는 sorted 함수이고,
리스트 자체를 정렬시켜버리는 것은 sort 함수입니다.
"""