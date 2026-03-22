t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    grid=[list(map(str,input().strip())) for _ in range(n)]
    #print(grid)
    breakset=set()
    crackpoint=set()
    for k in range(n):
        for i in range(n-1,-1,-1):
            #(i,k)
            if grid[i][k]=="#":
                crackpoint.add((i,k))#
                #print(i,k)
                break
    dp=[[0]*n for _ in range(n)]
    dp[n-1][c-1]=1
    dd=[-1,0,1]
    for i in range(n-1,0,-1):
        for k in range(n):
            if dp[i][k]==0:
                continue
            for qq in range(3):
                nn=i-1
                cc=k+dd[qq]
                if cc<0 or n-1<cc:
                    continue
                if (nn,cc) in crackpoint:
                    breakset.add(cc)
                if grid[nn][cc]=="." or cc in breakset:
                    dp[nn][cc]=1
    #print(dp)
    #print(breakset)
    ans=[]
    for i in range(n):
        ans.append(str(dp[0][i]))
    #print("".join(ans))
    print("".join(ans))