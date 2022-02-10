word = list(input())
count = []
for i in range(97,123):#a:97 ~ z:122
    ex = False
    for j in range(len(word)):
        if chr(i) == word[j]:
            count.append(j)
            ex = True
            break
        else:
            ex = False
    if ex == False:
        count.append(-1)

for i in range(0, len(count)):
    print(count[i], end=' ')

