n,m=map(int,input().split())
kyori=[[10**18]*(n+2) for _ in range(n+2)]
for i in range(m):
    a,b,c=map(int,input().split())
    kyori[a][b]=min(kyori[a][b],c)
    kyori[b][a]=min(kyori[b][a],c)
for i in range(n+2):
    kyori[i][i]=0
k,t=map(int,input().split())
D=list(map(int,input().split()))
for i in D:
    kyori[n+1][i]=t
    kyori[i][n+1]=0
for k in range(n+2):
  for i in range(n+2):
    for j in range(n+2):
      if kyori[i][j] > kyori[i][k] + kyori[k][j] : 
         kyori[i][j] = kyori[i][k] + kyori[k][j]
# for i in kyori:
#     print(i)
ans=0
for i in range(1,n+1):
    for k in range(1,n+1):
        if kyori[i][k]!=10**18:
            ans+=kyori[i][k]
q=int(input())

for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        x,y,tt=Q[1],Q[2],Q[3]
        if  tt<kyori[x][y]:
            ans-=2*kyori[x][y]
            kyori[x][y]=tt
            kyori[y][x]=tt
        else:
            continue
        for i in range(n+2):
            for j in range(n+2):
                if kyori[i][x]==10**18 or kyori[y][j]==10**18:
                    continue
                if kyori[i][j] > kyori[i][x] + tt + kyori[y][j] :
                    kyori[i][j] = kyori[i][x] + tt + kyori[y][j]
        for i in range(n+2):
            for j in range(n+2):
                if kyori[i][y]==10**18 or kyori[x][j]==10**18:
                    continue
                if kyori[i][j] > kyori[i][y] + tt + kyori[x][j] :
                    kyori[i][j] = kyori[i][y] + tt + kyori[x][j]
        
    elif Q[0]==2:
        x=Q[1]
        kyori[x][n+1]=0
        kyori[n+1][x]=t
        k=x
        for i in range(n+2):
            for j in range(n+2):
                if kyori[i][j] > kyori[i][k] + kyori[k][j] :
                    kyori[i][j] = kyori[i][k] + kyori[k][j]
        k=n+1
        for i in range(n+2):
            for j in range(n+2):
                if kyori[i][j] > kyori[i][k] + kyori[k][j] :
                    kyori[i][j] = kyori[i][k] + kyori[k][j]
        
    elif Q[0]==3:
        ans=0
        for i in range(1,n+1):
            for k in range(1,n+1):
                if kyori[i][k]!=10**18:
                    ans+=kyori[i][k]
        print(ans)
        
# for i in kyori:
#     print(i)