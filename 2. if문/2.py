#9498

def Bet(score):
    if(90<=score<=100):
        print("A")
    elif(80<=score<90):
        print("B")
    elif (70<=score<80):
        print("C")
    elif (60<=score<80):
        print("D")
    else:
        print("F")
def main():
    score = int(input())
    Bet(score)

main()