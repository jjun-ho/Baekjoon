#11022

test = int(input())
for i in range(1,test+1):
    n1, n2 = map(int,input().split())
    print( "Case #"+str(i)+":",n1,'+',n2,"=",n1+n2)