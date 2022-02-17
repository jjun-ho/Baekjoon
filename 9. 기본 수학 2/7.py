#1085

x, y, w, h =map(int,input().split())

dis = []
dis.append(x)
dis.append(y)
dis.append(w-x)
dis.append(h-y)
print(min(dis))

