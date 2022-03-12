#2751

import sys
n = int(input())
number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))
number.sort()
for i in number:
    print(i)

"""
* 선택 정렬
import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(i)
for last in reversed(range(1, len(data))):
    largset_index = 0
    for i in range(1,last+1):
        if data[i] > data[largset_index]:
            largset_index = i
    data[largset_index], data[last] = data[last], data[largset_index]

for i in data:
    print(i)
"""
