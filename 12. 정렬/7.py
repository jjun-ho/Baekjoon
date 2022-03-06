#11651

n = int(input())
where = []
for i in range(n):
    x, y = map(int, input().split())
    where.append((x, y))
where.sort(key=lambda x:x[0])
where.sort(key=lambda x:x[1])
# where.sort(key=lambda x:(x[1],x[0])) 위에 두줄 한줄로 표현하기
for i in where:
    print(i[0],i[1])
