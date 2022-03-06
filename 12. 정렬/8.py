#1181

n = int(input())
data = []
for i in range(n):
    data.append(input())
data = sorted(set(data))  #중복을 제거한 후 사전순 정렬
data.sort(key=len)
for i in data:
    print(i)

"""        
* set() 와 sort()
set() 함수를 이용하면 그 타입 그대로 기존 리스트에 저장해주지 않고, 기존 리스트의 순서는 고려하지 않고 중복을 제거하기 때문에 
sort() 함수를 연속적으로 사용 할 수 없다.
-> set() 함수를 사용한 값을 다른 변수에 저장해주고, 그 값을 리스트 다시 변환한 후 sort() 함수를 사용
-> Dictionary를 이용하여 key 값을 넣거나 sorted() 함수를 사용해야한다.

* 버블 정렬(시간 초과)
뒤에서 부터 앞으로 정렬을 해나가는 구조
맨 첫번째 값부터 시작해서 다음 값들과 차례로 비교하면서 앞의 값이 더 크면 뒤의 값과 자리를 바꾸면 됩니다.
거품 정렬은 점점 큰 값들을 뒤에서 부터 앞으로 하나씩 쌓여 나가게 때문에 후반으로 갈수록 정렬 범위가 하나씩 줄어들게 됩니다.
for i in range(len(data)):
    k = len(data) - i
    for j in range(1,k):
        if len(data[j-1]) > len(data[j]):
            temp = data[j-1]
            data[j-1] = data[j]
            data[j] = temp
"""
