#1181

n = int(input())
data = []
for i in range(n):
    string = input()
    data.append(string)
data = sorted(set(data))  #중복을 제거한 후 사전순 정렬
for i in range(len(data)):
    k = len(data) - i
    for j in range(1,k):
        if len(data[j-1]) > len(data[j]):
            temp = data[j-1]
            data[j-1] = data[j]
            data[j] = temp
for i in data:
    print(i)
"""        
set() 함수를 이용하면 기존 리스트의 순서는 고려하지 않고 중복을 제거하기 때문에 
sort() 함수를 연속적으로 사용 할 수 없다.
-> Dictionary를 이용하여 key 값을 넣거나 sorted() 함수를 사용해야한다.
"""
