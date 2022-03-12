#11650

n = int(input())
where = []
for i in range(n):
    x, y = map(int, input().split())
    where.append((x, y))
where.sort(key=lambda x: x[1])
where.sort(key=lambda x: x[0])
for i in where:
    print(i[0], i[1])