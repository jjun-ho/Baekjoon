#1676

import sys

def factorial(n):
    result = 1
    if n > 0:
        result = n * factorial(n-1)
    return result

n = int(sys.stdin.readline())
result = list(map(int, str(factorial(n))))
cnt = 0
for i in reversed(result):
    if i == 0:
        cnt += 1
    else:
        break
print(cnt)