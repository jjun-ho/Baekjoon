words = input(). upper()
word = list(set(words))

count = []
for x in word:
    cnt = words.count(x)
    count.append(cnt)
if count.count(max(count)) > 1 :
    print('?')
else:
    max = count.index(max(count))
    print(word[max])