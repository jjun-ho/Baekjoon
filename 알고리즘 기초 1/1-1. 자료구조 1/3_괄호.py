#9012

import sys

n = int(sys.stdin.readline())
for i in range(n):
    data = list(sys.stdin.readline())
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append('error')
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')