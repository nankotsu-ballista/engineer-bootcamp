n=int(input())
A=list(map(int,input().split()))
for i in range(n):
    A[i]=A[i]-1
visited=[False]*(n+1)
destination=[-1]*(n)
times=0
#print(A)
for i in range(n):
    if visited[i]!=False:
        continue
    nxt=i
    tmp=[]
    while visited[nxt]==False:
        visited[nxt]=True
        tmp.append(nxt)
        nxt=A[nxt]
    if destination[nxt]!=-1:
        nxt=destination[nxt]
    for i in tmp:
        destination[i]=nxt
#print(destination)
for i in range(len(destination)):
    destination[i]=destination[i]+1
print(*destination)
    
        
        
        
        