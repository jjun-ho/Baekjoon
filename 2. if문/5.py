def Bet(time, min):
    if (min < 45):
        if (time == 0):
            time = 23
            min = min + 60 - 45
        else:
            time -= 1
            min = min + 60 - 45
    elif (min > 45):
        min -= 45
    elif (min == 45):
        min = 0

    print(time, min)


def main():
    time, min = map(int, input().split())
    Bet(time, min)


main()