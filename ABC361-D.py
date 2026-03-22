from collections import deque
n=int(input())
s=input()
t=input()
t=t+".."
s=s+".."
t=list(t)
s=list(s)
SET=set()
q=deque()
def to_suji(S):
    sum=0
    S=list(S)
    for i in range(len(S)):
        if S[i]=="B":
            sum+=0*(3**i)
        if S[i]=="W":
            sum+=1*(3**i)
        if S[i]==".":
            sum+=2*(3**i)
    return(sum)
if s==t:
    print(0)
    exit()
answer=to_suji(t)
q.append((s,0))
while q:
    st,times=q.popleft()
    idx=0
    for i in range(len(st)):
        if st[i]==".":
            idx=i-1
    for i in range(len(st)-1):
        newS=[]
        for k in range(len(st)):
            newS.append(st[k])
        #print(newS)
        #print(idx)
        if st[i]!="." and st[i+1]!=".":
            newS[idx]=st[i]
            newS[idx+1]=st[i+1]
            newS[i]="."
            newS[i+1]="."
            tmp=to_suji(newS)
            if tmp not in SET:
                if tmp == answer:
                    print(times+1)
                    #print(newS)
                    exit()
                q.append((newS,times+1))
                SET.add(tmp)
print(-1)
    
    
    
    