#2588

def main():
    num1 = int(input())
    n1,n2,n3 = map(int, input())
    print(num1 *n3)
    print(num1 *n2)
    print(num1 *n1)
    print(num1*n3+num1*n2*10+num1*n1*100)

main()