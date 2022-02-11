#2739

def Count(num):
    for i in range(1,10):
        print(num,"*",i,"=",num*i)

def main():
    num=int(input())
    Count(num)

main()