#3052

import sys

list = []
data = [int(sys.stdin.readline()) for i in range(10)]
for i in data:
    list.append(i%42)
setlist = set(list)
print(len(setlist))

"""
* 입력의 모든것 
https://doing7.tistory.com/49

* set() 
중복된 데이터를 없애하고 하나의 데이터로 처리
"""

