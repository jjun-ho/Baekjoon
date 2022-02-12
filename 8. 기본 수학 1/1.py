#1712

A, B, C = map(int,input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))


"""
A+B*n = C*n
n= A/(C-B) : 수입과 비용 같아짐 -> 더 클 때:+1
"""