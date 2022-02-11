#1330

def Bet(n1,n2):
    if(n1>n2):
        print(">")
    elif(n1<n2):
        print("<")
    else:
        print("==")
def main():
    n1,n2= map(int,input().split())
    Bet(n1,n2)

main()