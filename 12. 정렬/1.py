#2750

n = int(input())
number = []
for i in range(n):
    num = int(input())
    number.append(num)
number.sort()
for i in number:
    print(i)

"""
sort 함수: 리스트명.sort( ) 형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정합니다.
sorted 함수: sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.
"""