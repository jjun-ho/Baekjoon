#10809

word = list(input())
count = []
for i in range(97,123):#a:97 ~ z:122
    ex = False
    for j in range(len(word)):
        if chr(i) == word[j]:
            count.append(j)
            ex = True
            break
        else:
            ex = False
    if ex == False:
        count.append(-1)

for i in range(0, len(count)):
    print(count[i], end=' ')

"""
* 리스트 한줄로 출력 
1. print의 end 속성
lst = [1,2,3,4,5,6,7,8,9]
for i in range(len(lst)):
    print(lst[i], end=' ')
#1 2 3 4 5 6 7 8 9 
2. join 사용
lst = [1,2,3,4,5,6,7,8,9]
print(' '.join(lst))
문자가 아닌 원소들로 이루어진 리스트는 join 함수 사용이 불가능하다.(숫자 x)

* fine() 함수 
find 함수를 이용해서 입력받은 문자열 안에 특정 문자가 있는지 찾는다.
find 함수는 문자열에서만 사용 가능한 함수이다. 이와 유사한 기능을 하는 함수로 index 함수가 있다. 
index 함수는 문자열뿐만 아니라 리스트, 튜플과 같은 반복 가능한 iterable 자료형에서도 찾는 문자의 인덱스를 반환하는 함수로 쓰인다. 
find 함수와 다른 점은 find 함수는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력하지만 index함수는 >AttributeError가 발생한다.

* index() 
특정 문자의 인덱스 리턴
"""