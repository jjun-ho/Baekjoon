test = int(input())

for k in range(test):
    num, data = input().split()
    num = int(num)
    data = list(data)

    result = []
    string = " "
    for j in data:
        for i in range(num):
            result.append(j)
    string = "".join(result)
    print(string)

