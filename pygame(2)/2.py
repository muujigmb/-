import random
f=open("voca.txt","r",encoding='UTF-8')
raw_data=f.read()
f.close
print(raw_data.split('\n')[-1])
data_list=raw_data.split('\n')
data_list=data_list[:-1]
while True:
    r_index=random.randrange(0,len(data_list))
    word=data_list[r_index].replace(u'\xa0',u' ').split(' ')[1]
    if len(word) <= 6:break
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
        print(word)
        break
    if word_show.find('_')==-1 :
        print('유저 승')
        print(word)
        break