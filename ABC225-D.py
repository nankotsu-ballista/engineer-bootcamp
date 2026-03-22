n,q=map(int,input().split())
forward=[-1]*(n+1)
back=[-1]*(n+1)
for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        x=Q[1]
        y=Q[2]
        forward[y]=x
        back[x]=y
    elif Q[0]==2:
        x=Q[1]
        y=Q[2]
        back[x]=-1
        forward[y]=-1
    elif Q[0]==3:
        x=Q[1]
        forwardest=x
        while forward[forwardest]!=-1:
            forwardest=forward[forwardest]
        ans=[forwardest]
        while back[forwardest]!=-1:
            forwardest=back[forwardest]
            ans.append(forwardest)
        print(*[len(ans)]+ans)
