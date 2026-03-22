from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    C=[-1]+list(map(int,input().split()))
    dp=[[10**18]*(n+1) for _ in range(n+1)]
    nodes=[[]for _ in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    # for i in range(n):
    #     for k in range(n):
    #         if C[i]!=C[k]:
    #             dp[i][k]=True
    dp[1][n]=0
    q=deque()
    q.append((1,n,0))
    while q:
        takahashi,aoki,times=q.popleft()
        tmptaka=[]
        tmpaoki=[]
        for i in nodes[takahashi]:
            if C[i]==0:
                tmptaka.append(i)
        for i in nodes[aoki]:
            if C[i]==1:
                tmpaoki.append(i)
        for i in tmptaka:
            for k in tmpaoki:
                if dp[i][k]>times+1:
                    q.append((i,k,times+1))
                    dp[i][k]=times+1
        
        tmptaka=[]
        tmpaoki=[]
        for i in nodes[takahashi]:
            if C[i]==1:
                tmptaka.append(i)
        for i in nodes[aoki]:
            if C[i]==0:
                tmpaoki.append(i)
        for i in tmptaka:
            for k in tmpaoki:
                if dp[i][k]>times+1:
                    q.append((i,k,times+1))
                    dp[i][k]=times+1
    
    if dp[n][1]!=10**18:
        print(dp[n][1])
    else:
        print(-1)