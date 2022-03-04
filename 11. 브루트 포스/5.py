#1436

n = int(input())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1

"""
1. 666
2. 1666
3. 2666
4. 3666
5. 4666
6. 5666
7. 6660
8. 6661 ...
"""