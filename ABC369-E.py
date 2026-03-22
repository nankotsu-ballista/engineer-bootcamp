import itertools
n,m=map(int,input().split())
distance=[[10**12]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    distance[i][i]=0
bridge=[(-1,-1,-1)]
for _ in range(m):
    u,v,t=map(int,input().split())
    distance[u][v]=min(t,distance[u][v])
    distance[v][u]=min(t,distance[v][u])
    bridge.append((u,v,t))
#print(bridge)
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
q=int(input())
for i in range(q):
    ans=10**12
    k=int(input())
    B=list(map(int,input().split()))
    p = itertools.permutations(B)
    for T in p:
        
        tmpbridges=[]
        for i in T:
            tmpbridges.append((bridge[i]))
        #print(tmpbridges)
        for c in range(1<<k):
            tmp=0
            before=1
            #print("before",before)
            for d in range(k):
                if c>>d & 1:
                    tmp+=distance[before][tmpbridges[d][0]]
                    tmp+=tmpbridges[d][2]
                    before=tmpbridges[d][1]
                else:
                    tmp+=distance[before][tmpbridges[d][1]]
                    tmp+=tmpbridges[d][2]
                    before=tmpbridges[d][0]
            tmp+=distance[before][n]
            ans=min(ans,tmp)
    print(ans)
            
            
    