#11727

s = [0, 1, 3]
for i in range(3, 1001):
  s.append((s[i - 2]*2) + s[i - 1])
n = int(input())
print(s[n] % 10007)

"""
n = 1일때 방법의 수는 1개.
n = 2 - 3개
n = 3 - 5개
n = 4 - 11개
n = 5 - 21개
n의 방법의 수  = (n-1) + (n-2)*2
"""