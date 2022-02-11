N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result-=1
            break
print(result)


"""
파이썬 pass와 continue 차이점
* pass는 실행할 것이 아무 것도 없다는 것을 의미한다.
따라서 아무런 동작을 하지 않고 다음 코드를 실행한다.
사실상 없는 것과 차이가 없는데, 그러면 왜 쓰는가? 소스코드 블럭이 있다는 표시로 쓴다.
* 반면 continue는 다음 순번의 loop 실행한다.
"""