#2675

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

"""
* join() 
a = [“a/b/c”, “d”, “e”]
1. 리스트 배열을 문자열로 합치기
	“”.join(a)
	a/b/cde 
2. 요소 사이에 특정 문자열을 추가하여 문자열로 변환
	ex) 요소 사이에 특정 문자열을 추가하여 문자열로 변환
	‘/‘.join(a)
	a/b/c/d/e

* 한줄에 숫자 , 문자 나눠서 입력받기 
num, data = input().split()
"""