#11729

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi_tower(n - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계

n = int(input())
print(2 ** n - 1)
hanoi_tower(n, 1, 3)

"""
1단계 에서는 n-1개의 원판을 1번 막대에서 2번 막대로 옮깁니다.
2단계 에서는 남은 1개의 원판을 1번 막대에서 3번 막대로 옮깁니다.
3단계 에서는 다시 n-1개의 원판을 2번 막대에서 3번 막대로 옮깁니다.

* 파이썬 하노이 
https://youtu.be/FYCGV6F1NuY
"""