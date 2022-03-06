#18870

import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []
arr2 = list(sorted(set(arr))) #중복 제거하고 오름차순 정렬한 리스트
dic = {arr2[i]:i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')

"""
* 파이썬 Dictionary
1. 딕셔너리이름 = {"key값" : "value값"} 
2. key 중복 허용 X
3. key가 중복 될 경우 마지막에 입력된 key의 value를 출력.
ex1)
a = {"key1":"value1", "key2":"value2", "key1":"value3"}
print(a["key1"])
-> value3
ex2)
dic = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4",} 
print(dic["key1"]) 
-> value1

* Dictionary 사용x(시간 초과)
import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(n):
    result.append(-1)
grade = 0
for i in range(min(data),max(data)+1):
    if i in data:
        for j in range(len(data)):
            if i == data[j]:
                result[j] = grade
        grade += 1
for i in result:
    if i == -1:
        break
    print(i, end=' ')
"""