#2108

import sys
from collections import Counter
n = int(input())
number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))
sorted_number = sorted(number)
cnt = Counter(sorted_number).most_common()
print(round(sum(sorted_number)/n)) #산술평균
print(sorted_number[n//2]) #중앙값
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]: #최빈값
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(max(number)-min(number))  #범위

"""
* counter 함수
from collections import Counter
반환값이 dictionary 형태이다
입력도 가능함:Counter({'C':3,'B':2,'A':1})
->['A','B','B','C','C','C']
most_common()
Counter(list).most_common()
Counter()에서 가장 빈도수가 높은 순으로 표시해 주는 함수이다. 
단, 인자값으로 숫자를 입력하시면 그 숫자번째까지의 빈도수를 표시해준다.
빈도수가 같을 때에는 인자로 받은 리스트에서 먼저 들어간 순서대로 출력한다.
"""