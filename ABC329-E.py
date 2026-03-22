from collections import deque
n,m=map(int,input().split())
S=list(input())
T=list(input())
i=0
q=deque()
visited=[False]*(n+1)
while i<n-m+1:
    i+=1
    cnt=0
    for k in range(m):
        if S[i-1+k]==T[k]:
            cnt+=1
    if cnt==m:
        q.append(i-1)
        visited[i-1]=True
        for k in range(m):
            S[i-1+k]="#"
#print(S)
        
#print(q)
while q:
    idx=q.popleft()
    for i in range(-m,m):
        husecount=0
        count=0
        if visited[idx+i]==True:
            continue
        
        if -1<(idx+i) and (idx+i)<n-m+1:
            for k in range(m):
                if S[idx+i+k]==T[k]:
                    count+=1
                if S[idx+i+k]=="#":
                    count+=1
                    husecount+=1
            if husecount==m:
                visited[idx+i]=True
                continue
            if count==m:
                q.append(idx+i)
                for k in range(m):
                    S[idx+i+k]="#"
for i in S:
    if i != '#':
        print("No")
        exit()
print("Yes")
                
        
    
    
        