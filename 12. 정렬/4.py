#2108

import sys
n = int(input())
number = []
cnt = []
max_number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))
sorted_number = sorted(number)
for i in sorted_number:
    cnt.append(number.count(i))
max_index = cnt.index(max(cnt))
mid_index = int((n-1)/2)
for i in number:
    if i == max(cnt):
        max_number.append(i)



print(int(round(sum(sorted_number)/n)))
print(sorted_number[mid_index])
print(number[max_index])
print(max(sorted_number)-min(sorted_number))

