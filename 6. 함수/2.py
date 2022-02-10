def d(n):
    data = list(map(int, str(n)))
    n = n + sum(data)
    return n


numbers = list(range(1, 10001))
remove_list = []
for i in range(1, 10001):
    remove_list.append(d(i))
for j in range(1, 10001):
    if j not in remove_list:
        print(j)
