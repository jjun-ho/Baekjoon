#1018

n, m = map(int, input().split())
data = []
cnt = []
for i in range(n):
    data.append(input())
for a in range(n-7):
    for b in range(m-7):
        index1 = 0  #흰색으로 시작한 경우의 값을 초기화
        index2 = 0  #검은색으로 시작한 경우의 값을 초기화
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0: #행과 열의 인덱스 합 짝수
                    if data[i][j] != 'W':
                        index1 += 1
                    if data[i][j] != 'B':
                        index2 += 1
                else:              #행과 열의 인덱스 합 홀수
                    if data[i][j] != 'B':
                        index1 += 1
                    if data[i][j] != 'W':
                        index2 += 1
        cnt.append(min(index1, index2))
print(min(cnt))

"""
 (i + j) %2 == 0을 사용했는데, 
 이 이유는, 행과 열의 인덱스의 합이 짝수인경우 일정한 한 색을 가지게 되고, 
 홀수인 경우에도 다른 일정한 한 색을 가지게 된다.
0(짝)	1(홀)	2(짝)	3(홀)
1(홀)	2(짝)	3(홀)	4(짝)
2(짝)	3(홀)	4(짝)	5(홀)
3(홀)	4(짝)	5(홀)	6(짝)
"""