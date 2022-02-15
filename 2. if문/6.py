#2525

a, b = map(int, input().split())
time = int(input())
result_a = a
result_b = b+time

while result_b >= 60:
    if result_b >= 60:
        result_a += 1
        result_b -= 60
        if result_a == 24:
            result_a = 0

print(result_a, result_b)