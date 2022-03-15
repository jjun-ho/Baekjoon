#1934

import sys
n = int(sys.stdin.readline())
for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    a, b = n1, n2

    while b != 0:
        a = a % b
        a, b = b, a
    print(n1*n2//a)  # 최소 공배수 lcm

