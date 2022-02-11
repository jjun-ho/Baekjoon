alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()


for i in alpha:
        word = word.replace(i, '*')

print(len(word))

"""
* replace 
문자를 변환하는 함수.
replace함수는 함수를 사용한 문자열 원형을 변형시키지 않는 비파괴적 함수이기 때문에 저장하는 변수를 동일한 변수로 사용
"""