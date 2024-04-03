import random as r
a='이영광','강병철','이종규','김강민','남현준','성원우','박효열','최태양'
print('보기 : "이영광, 강병철, 이종규, 김강민, 남현준, 성원우, 박효열, 최태양"')
word=r.choice(a)
word=word.upper()
word_show="_"*len(word)
try_number=0
ok=[]
no=[]
while True:
    ans=input().upper()
    result=word.find(ans)
    if result==-1:
        print('오답')
        try_number+=1
        no.append(ans)
    else:
        print('정답')
        ok.append(ans)        
        for i in range(len(word)):
            if (word[i]==ans) :
                word_show=word_show[:i]+ans+word_show[i+1:]
            elif (word[:]==ans):
                word_show=ans   
        print(word_show)
        
    if try_number==7:
        print('컴퓨터 승')
        break
    if word_show.find('_')==-1 :
        print('유저 승')
        break
print(word)