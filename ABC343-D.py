N,T=map(int,input().split())
score ={}
player =[0]*(N+1)
score[0]=N
for i in range(T):
    A,B=map(int,input().split())
    score[player[A]]-=1
    if score[player[A]]==0:
        del score[player[A]]
    player[A] += B
    if player[A] in score:
        score[player[A]]+=1
    else:
        score[player[A]]=1
    #print(score)
    print(len(score))
#print(score)

