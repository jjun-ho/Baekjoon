#1427

import math
num = str(input())
num = list(map(int, num))
num.sort()
result = 0
for i in reversed(range(len(num))):
    result += num[i]*int(math.pow(10,i))
print(result)

"""
* 리스트에 map() 함수
map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환합니다.
그다음에 list를 사용해서 map의 결과를 다시 리스트로 만들어줍니다.

* sort() 함수의 내림차순
리스트.sort(reverse=False) 인 게 디폴트여서 리스트가 오름차순으로 정렬이 되는 것이고
리스트.sort(reverse=True)로 변경하면 리스트가 내림차순으로 정렬이 됩니다.

* math.pow 함수
import math를 통해서 math 라이브러리를 임포트 해야 합니다.
함수 모양 : math.pow(x, y)
함수 설명 : math.pow(x, y) 함수는 x의 y 거듭제곱 (x의 y승)을 반환합니다.
1. 이 함수의 반환형은 언제나 float 타입입니다. (정수 타입 계산을 원한다면 내장 함수 pow 혹은 ** 을 사용하면 됩니다.)
2. 주의할 점은 x가 음수이면서 y가 실수를 집어넣은 경우에는 Error 가 나옵니다. ( math.pow (-2, 3.2) 이런 식은 에러)
"""