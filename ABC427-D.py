t=int(input())
for times in range(t):
    n,m,k=map(int,input().split())
    s=input()
    nodes=[[] for _ in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        nodes[u-1].append(v-1)
    dp=[[False]*n for _ in range(2*k+1)]
    for ab in range(len(s)):
        if s[ab]=="A":
            dp[2*k][ab]=True
    # print(nodes)
    # print(dp)
    for i in range(2*k,0,-1):
        if i%2==0:
            for j in range(n):
                for c in nodes[j]:
                    if dp[i][c]==False:
                        dp[i-1][j]=False
                        break
                    else:
                        dp[i-1][j]=True
        elif i%2==1:
            for j in range(n):
                for c in nodes[j]:
                    if dp[i][c]==True:
                        dp[i-1][j]=True
                        break
                    else:
                        dp[i-1][j]=False
    if (dp[0][0]) ==True:
        print("Alice")
    else:
        print("Bob")