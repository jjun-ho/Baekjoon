#10814

n = int(input())
data = []
for i in range(n):
    age, name =input().split()
    data.append((age, name))
data.sort(key=lambda x: int(x[0]))
for i in data:
    print(i[0],i[1])