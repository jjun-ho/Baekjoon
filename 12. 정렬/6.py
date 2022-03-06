#11650

n = int(input())
where = []
for i in range(n):
    x, y = map(int, input().split())
    where.append((x, y))
where.sort(key=lambda x:x[1])
where.sort(key=lambda x:x[0])
for i in where:
    print(i[0],i[1])

"""
* 튜플 정렬하기
v = [(3,4), (2,2), (3,3), (1,2), (1,-1)]
1. 첫 번째 원소로 오름차순 정렬하기
v.sort(key = lambda x:x[0])
-> v = [(1,2), (1,-1), (2,2), (3,4), (3,3)]
2. 첫 번째 원소로 내림차순 정렬하기
v.sort(key = lambda x:-x[0])
v.sort(key = lambda x:x[0], reverse=True)
-> v = [(3,4), (3,3), (2,2), (1,2), (1,-1)]
3. 두 번째 원소로 오름차순 정렬하기
v.sort(key = lambda x:x[1])
-> v = [(1,-1), (2,2), (1,2), (3,3), (3,4)]
4. 첫 번째 원소로 오름차순 정렬하고, 첫 번째 원소가 같은 경우 두 번째 원소로 오름차순 정렬하기
v.sort()
v.sort(key = lambda x:(x[0],x[1]))
-> v = [(1,2), (1,-1), (2,2), (3,4), (3,3)]
5. 첫 번째 원소로 내림차순 정렬하고, 첫 번째 원소가 같은 경우 두 번째 원소로 오름차순 정렬하기
v.sort(key = lambda x:(-x[0],x[1]))
-> v = [(3,3), (3,4), (2,2), (1,-1), (1,2)]
"""