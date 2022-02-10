import sys

data= []
avg = 0
n = int(input())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    count =0
    avg = (sum(data[i])-data[i][0])/data[i][0]
    for j in range(1,data[i][0]+1):
        if (avg < data[i][j]):
            count += 1
    result = (count/data[i][0])*100
    s_result = '{:.3f}'.format(result)
    print(s_result+'%')


