#1406

import sys
s1 = list(sys.stdin.readline().strip()) #corsor 기준 두개의 스택으로 나눔
s2 = []
n = int(sys.stdin.readline())
cursor = len(s1)
for i in range(n):
    com = sys.stdin.readline().strip()
    if com[0] == 'P':
        s1.append(com[2]) # 첫번째 스택에 추가
    elif com[0] == 'L' and s1 != []:
        s2.append(s1.pop()) # 커서가 왼쪽으로 간다 = 첫 스택에서 pop 한거를 두번째로 옮겨줌, 두번쨰 스택에는 역순으로 저장(첫번째에 끝부터 저장)
    elif com[0] == 'D' and s2 != []:
        s1.append(s2.pop()) # 커서가 오른쪽으로 간다 = 두번째 스택에서 pop 한거를 첫번째로 옮겨줌
    elif com[0] == 'B' and s1 != []:
        s1.pop()
print(''.join(s1+list(reversed(s2))))  # 두번째 스택에는 순서가 반대로 저장되어있음

"""
*  append( ) / extend( ) / insert( ) 차이
1. list.append(x)
append는 덧붙인다는 뜻으로 새로운 요소를 list 맨 끝에 객체로 추가한다.
ex) 
nums = [1, 2, 3]
nums.append([5, 6])
>[1, 2, 3, 4, [5, 6]] # 리스트가 하나의 객체로 추가되었음

2. list.extend(iterable)
append와 동일하게 요소를 array의 끝에 추가하지만, 
append와 다른 점은 괄호( ) 안에는 iterable 자료형만 올 수 있다는 것이다.
ex)
nums = [1, 2, 3]
nums.extend([4, 5])
>[1, 2, 3, 4, 5]  #리스트로 주어진 [4, 5]의 요소가 각각 추가 되었음

3. list.insert(i, x)
list의 원하는 위치 i 앞에 추가할 값 x를 삽입할 수 있다. 
i는 위치를 나타내는 인덱스를 숫자를 입력한다.
음수를 입력하면 배열의 끝을 기준으로 처리된다.
ex)
nums = [1, 2, 3]
nums.insert(0, [10, 20])  # 0번째(맨앞에) 추가
>[[10, 20], 1, 2, 3]
nums.insert(-1, 100)  # 끝에서 1번째 전에 추가
>[[10, 20], 1, 2, 100, 3]  # 리스트 맨 끝에 저장되지 않음
"""