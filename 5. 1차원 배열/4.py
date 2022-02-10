import sys

list = []
data = [int(sys.stdin.readline()) for i in range(10)]
for i in data:
    list.append(i%42)
setlist = set(list)
print(len(setlist))



