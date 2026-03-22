from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    nodes[x].append((y,z))
    nodes[y].append((x,z))
bits=[30*[-1] for _ in range(n+1)]
q=deque()
for k in range(30):
    for i in range(n+1):
        if bits[i][k]!=-1:
            continue
        onezero=[[] for _ in range(2)]
        q.append(i)
        bits[i][k]=0
        onezero[0].append(i)
        while q:
            idx=q.popleft()
            for j,z in nodes[idx]:
                if bits[j][k]==-1:
                    q.append(j)
                    if z&(1<<k):
                        bits[j][k]=(bits[idx][k]+1)%2
                        onezero[bits[j][k]].append(j)
                    else:
                        bits[j][k]=bits[idx][k]
                        onezero[bits[j][k]].append(j)
                else:
                    if z&(1<<k):
                        if bits[j][k]==bits[idx][k]:
                            print(-1)
                            exit()
                    else:
                        if bits[j][k]!=bits[idx][k]:
                            print(-1)
                            exit()
        if len(onezero[0])>len(onezero[1]):
            for f in onezero[0]:
                bits[f][k]=0
            for f in onezero[1]:
                bits[f][k]=1
        else:
            for f in onezero[0]:
                bits[f][k]=1
            for f in onezero[1]:
                bits[f][k]=0
anss=[]
# for i in bits:
#     print(i)
for i in range(1,n+1):
    tmp=0
    for k in range(30):
        tmp+=bits[i][k]*2**k
    anss.append(tmp)
print(*anss)
    
    
    
    
    
    
    
    
    
    
    
    
    
            