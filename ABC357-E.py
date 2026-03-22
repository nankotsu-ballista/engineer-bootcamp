from collections import deque
n=int(input())
A=list(map(int,input().split()))
nyujisu=[0]*(n+1)
tmpnyujisu=[0]*(n+1)
for i in range(n):
    nyujisu[A[i]]+=1
    tmpnyujisu[A[i]]+=1
#print(nyujisu)
q=deque()
for i in range(1,n+1):
    if tmpnyujisu[i]==0:
        q.append(i)
A=[0]+A
while q:
    nxt=q.popleft()
    tmpnyujisu[A[nxt]]-=1
    if tmpnyujisu[A[nxt]]==0:
        q.append(A[nxt])
#print(tmpnyujisu)
visited=[False]*(n+1)
for i in range(n+1):
    if tmpnyujisu[i]==0:
        visited[i]=True
#print(A)
ans=0
cyclesize=[0]*(n+1)
for i in range(1,n+1):
    if visited[i]==True:
        continue
    tmp=[]
    q=deque()
    tmp.append(i)
    q.append(i)
    visited[i]=True
    while q:
        nxt=q.popleft()
        if visited[A[nxt]]==False:
            visited[A[nxt]]=True
            q.append(A[nxt])
            tmp.append(A[nxt])
    #print(tmp)
    sd=len(tmp)
    ans+=sd*sd
    for t in tmp:
        cyclesize[t]=sd
    
#print(cyclesize)
#print(nyujisu)

q=deque()
edasize=[-1]*(n+1)
for i in range(n+1):
    if cyclesize[i]!=0:
        edasize[i]=0
        
#print(edasize)
for i in range(1,n+1):
    if nyujisu[i]==0:
        q.append(i)
    eda=[]
    
    while q:
        idx=q.popleft()
        eda.append(idx)
        if edasize[A[idx]]==-1:
            q.append(A[idx])
            
    #print(eda)
    if len(eda)==0:
        continue
    tmpcycle=cyclesize[A[idx]]
    root=edasize[A[idx]]
    eda.reverse()
    for i in range(len(eda)):
        edasize[eda[i]]=i+1+root
        cyclesize[eda[i]]=tmpcycle
# print(edasize)
# print(cyclesize)
# print(ans)
ans=0
for i in range(1,n+1):
    ans+=cyclesize[i]+edasize[i]
print(ans)
    
        
    
        

            
        
    

    
