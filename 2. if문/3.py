#2753

def Bet(year):
    if(year%4==0):
        if(year%100 !=0):
            print('1')
        elif (year % 400 == 0):
            print('1')
        else:
            print('0')
    else:
        print('0')

def main():
    year = int(input())
    Bet(year)

main()