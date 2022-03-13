#10825

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    data.append((name, kor, eng, math))
data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for j in data:
    print(j[0])