#10866

from collections import deque
import sys
d = deque()
n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:  # 비어있지 않으면 = 상수 = True
            print(d.popleft())  # popleft 후 print(d[0])
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
            print(d.pop())  # pop 후 print(d[len(d)-1])
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])  # print(d[-1])
        else:
            print("-1")

"""
* collections.deque 의 함수들
import deque
1. collections.deque.append(x)
list.append 처럼 맨 뒤 (오른쪽) 에 삽입 해준다
ex)
from collections import deque 
dq = deque([1,2,3,4]) 
dq.append('a')
print(dq)
>deque([1,2,3,4,'a'])

2. collentions.deque.appendleft(x)
deque 의 왼쪽에 삽입해준다

3. collections.deque.clear()
deque 안의 모든 요소를 제거해준다

4. collections.deque.insert(i,x)
i 번째 index 에 x 를 삽입해준다 

5. collections.deque.pop()
맨 오른쪽 을 제거해주며 제거한 값을 return 해준다

6. ollections.deque.popleft()
맨 왼쪽을 제거해주며 제거한 값을 return 해준다
"""