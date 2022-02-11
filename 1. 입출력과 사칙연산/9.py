#10869

def A(n1,n2):
    return n1 + n2

def B(n1,n2):
    return n1-n2

def C(n1,n2):
    return n1*n2

def D(n1,n2):
    return int(n1/n2)

def E(n1,n2):
    return n1%n2

def main():
    n1,n2 = map(int, input().split())
    print(A(n1,n2))
    print(B(n1,n2))
    print(C(n1,n2))
    print(D(n1,n2))
    print(E(n1,n2))
main()