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

"""
* round(반올림하고자 하는 값, 자릿수) 
소수점 몇 자리까지 반올림
다만 round(40.0000000,3) 하면 40.000 안되고 자동으로 40.0으로 변함
{:.자릿수f).format(반올림하고자 하는 값)사용하면 가능
"""
