def A(n1,n2,n3):
    return (n1+n2)%n3

def B(n1,n2,n3):
    return ((n1%n3)+(n2%n3))%n3

def C(n1,n2,n3):
    return (n1*n2)%n3

def D(n1,n2,n3):
    return ((n1%n3)*(n2%n3))%n3


def main():
    n1,n2,n3 = map(int, input().split())
    print(A(n1,n2,n3))
    print(B(n1,n2,n3))
    print(C(n1,n2,n3))
    print(D(n1,n2,n3))
main()