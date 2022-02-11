#1157

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

"""
* upper() 
대문자로 바꿈

* set() 
문자열 중 중복되는 요소 제거 

* get(a, b) 
첫번째 인자에 해당 찾고 싶은 딕셔너리 key 값 입력하고, 두번째 인자에는 첫번째 인자가 없을 경우 출력하고 싶은 값 입력. key값의 value 값 출력

"""