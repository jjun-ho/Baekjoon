#2231

n = int(input())
result = 0
for i in range(1, n+1): #1부터 n까지
    data = list(map(int, str(i)))
    result = i + sum(data)
    if result == n: #생성자 있는 경우
        print(i)
        break
    if i == n: #생성자 없는 경우
        print(0)
