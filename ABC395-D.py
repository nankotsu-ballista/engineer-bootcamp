n,q=map(int,input().split())
suposition=[]
sulabel=[]
hato=[]
for i in range(n+1):
    suposition.append(i)
    sulabel.append(i)
    hato.append(i)
    
for i in range(q):
    S=list(map(int,input().split()))
    if S[0]==1:
        a=S[1]
        b=S[2]
        hato[a]=suposition[b]
    elif S[0]==2:
        a=S[1]
        b=S[2]
        sulabel[suposition[a]],sulabel[suposition[b]] = sulabel[suposition[b]],sulabel[suposition[a]] 
        suposition[a], suposition[b] = suposition[b], suposition[a]
    elif S[0]==3:
        a=S[1]    
        print(sulabel[hato[a]])
# print(suposition)
# print(sulabel)
# print(hato)


    