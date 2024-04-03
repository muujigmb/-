A=(10.1, -1.2)

def tup_r(tup):
    #2. 리스트 만들기
    temp_list=[]
    #3. tup을 a로 변환한 다음에 a를 반올림한 다음 리스트에 추가 시켜준다.
    for a in tup:
        temp_list.append(round(a))
    #4. 리스트값을 투플값으로 변환한 다음에 리턴, 즉 다시 호출한 곳으로 돌려보낸다.
    return tuple(temp_list)
#1. tup_r을 호출한다.
print(tup_r(A))