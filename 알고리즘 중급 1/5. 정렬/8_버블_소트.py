#1377

import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))
sorted_arr = sorted(arr)
answer = []
for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])
print(max(answer) + 1)

"""
*  버블 정렬
뒤에서 부터 앞으로 정렬을 해나가는 구조
맨 첫번째 값부터 시작해서 다음 값들과 차례로 비교하면서 앞의 값이 더 크면 뒤의 값과 자리를 바꾸면 됩니다.
거품 정렬은 점점 큰 값들을 뒤에서 부터 앞으로 하나씩 쌓여 나가게 때문에 후반으로 갈수록 정렬 범위가 하나씩 줄어들게 됩니다.

정렬되기 후에서 정렬되기 전(인덱스 값) 뺄셈을 해보면 음수인 경우는 뒤로 이동, 양수인 경우는 앞으로 이동한 칸 수가 나온다.
그리고 그 값들의 최대값이 버블정렬이 몇회차까지 필요한지를 나타내게 된다. 위의 예에서는 +1이 최대값이다.
"""