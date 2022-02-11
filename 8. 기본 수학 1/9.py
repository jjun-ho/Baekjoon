T = int(input())
#(1 2) (33 44) (555 666) (7777 8888) (99999
for i in range(T):
    x, y = map(int, input().split())
    distance=int(y)-int(x)
    space=0
    k=0
    a=0.5
    while distance > k:
        a=a+0.5
        k=k+int(a)
        space=space+1

    print(space)

