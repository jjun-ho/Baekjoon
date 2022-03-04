#7568

n = int(input())
data = []
grade = []
for i in range(n):
    x, y = map(int,input().split())
    data.append([x,y])
for i in range(len(data)):
    cnt = 0
    for j in range(0,len(data)):
        if (data[i][0] < data[j][0]) and (data[i][1] < data[j][1]):
            cnt += 1
    grade.append(cnt+1)
for i in grade:
    print(i, end=" ")

"""
*  print() 줄바꿈 제거
for i in grade:
    print(i, end=" ")
"""