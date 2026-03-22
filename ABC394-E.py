from collections import deque
n=int(input())
C=[list(map(str,input().strip())) for _ in range(n)]
nodes=[[[] for _ in range(n+1)]for _ in range(n+1)]
for i in range(n):
    for k in range(n):
        if C[i][k]!="-":
            nodes[n][n].append((i,k,1))
for i in range(n):
    nodes[n][n].append((i,i,0))
            
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             for l in range(n):
#                 if C[i][j]==C[k][l] and C[i][j]!="-":
#                     nodes[j][k].append((i,l,2))
q=deque()
costs=[[10002]*(n+1) for _ in range(n+1)]
costs[n][n]=0
for i in range(n):
    costs[i][i]=0
    q.append((i,i))
for i in range(n):
    for k in range(n):
        if i!=k and C[i][k]!="-":
            costs[i][k]=1
            q.append((i,k))
#print(q)
while q:
    i,k=q.popleft()
    #print(i)
    for cd in range(n):
        for nd in range(n):
            if C[cd][i]==C[k][nd] and C[cd][i]!="-" and costs[cd][nd]>costs[i][k]+2:
                costs[cd][nd]=costs[i][k]+2
                q.append((cd,nd))
    
                
for i in range(n):
    tmp=[]
    for k in range(n):
        if costs[i][k]==10002:
            tmp.append(-1)
        else:
            tmp.append(costs[i][k])
    print(*tmp)
    
    