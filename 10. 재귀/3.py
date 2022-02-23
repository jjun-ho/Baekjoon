#2447

# 별 찍는 재귀 함수
def draw_star(n):
    global Map
    if n == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return
    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]  # 핵심

N = int(input())
Map = [[0 for i in range(N)] for i in range(N)]  # 메인 데이터 선언
draw_star(N)
for i in Map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

"""
* 핵심 ex) n = 9 Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]
i j k a
0 0 ? 3  Map[k][0:3] = Map[k][:3]
0 1 ? 3  Map[k][3:6] = Map[k][:3]
0 2 ? 3  Map[k][6:9] = Map[k][:3]
1 0 ? 3  Map[3 + k][0:3] = Map[k][:3]
1 1 ? 3  Map[3 + k][3:6] = Map[k][:3] ** 빈공간 **
1 2 ? 3  Map[3 + k][6:9] = Map[k][:3] 
2 0 ? 3  Map[6 + k][0:3] = Map[k][:3]
2 1 ? 3  Map[6 + k][3:6] = Map[k][:3] 
2 2 ? 3  Map[6 + k][6:9] = Map[k][:3]
"""