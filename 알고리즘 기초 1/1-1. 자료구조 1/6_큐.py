#10845

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    com = list(sys.stdin.readline().split())
    if com[0] == 'push':
        data.append(int(com[1]))
    elif com[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
            data.remove(data[0])
    elif com[0] == 'front':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif com[0] == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[len(data)-1])
    elif com[0] == 'size':
        print(len(data))
    elif com[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)