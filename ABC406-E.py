t=int(input())
for _ in range(t):
    n,kk=map(int,input().split())
    ns=[]
    keta=60
    for i in range(keta):
        if n&(1<<i):
            ns.append(1)
        else:
            ns.append(0)
    ns.reverse()
    #print(ns)
    dp=[[[0]*(2) for _ in range(keta+1)]for _ in range(keta+1)]
    dp[0][0][1]=1
    ans=0
    mod=998244353
    ans=0
    for i in range(keta):
        for k in range(keta):
            if ns[i]==1:
                if k>kk:
                    continue
                dp[i+1][k][0]+=dp[i][k][0]
                dp[i+1][k][0]+=dp[i][k][1]
                dp[i+1][k][0]=dp[i+1][k][0]%mod
                if k==0:
                    continue
                dp[i+1][k][0]+=dp[i][k-1][0]
                dp[i+1][k][0]=dp[i+1][k][0]%mod
                dp[i+1][k][1]+=dp[i][k-1][1]
                dp[i+1][k][1]=dp[i+1][k][1]%mod
            elif ns[i]==0:
                if k>kk:
                    continue
                dp[i+1][k][0]+=dp[i][k][0]
                dp[i+1][k][1]+=dp[i][k][1]
                dp[i+1][k][1]=dp[i+1][k][1]%mod
                if k==0:
                    continue
                dp[i+1][k][0]+=dp[i][k-1][0]
                dp[i+1][k][0]=dp[i+1][k][0]%mod
    # for i in dp:
    #     print(i)
    ndp=[[0 for _ in range(keta+1)]for _ in range(keta+1)]
    lis=[0]
    tn=0
    for i in range(keta):
        tn+=ns[i]*2**(keta-i-1)
        lis.append(tn)
    #print(lis)
    count=0
    for i in range(keta):
        if ns[i]==1:
            ndp[i+1][count]=(ndp[i+1][count]+lis[i])%mod
            count+=1
        for k in range(keta):
            ndp[i+1][k+1]=ndp[i+1][k+1]+ndp[i][k]+dp[i][k][0]*(2**(keta-i-1))
            ndp[i+1][k+1]=ndp[i+1][k+1]%mod
            ndp[i+1][k]=ndp[i+1][k]+ndp[i][k]
            ndp[i+1][k]=ndp[i+1][k]%mod
            
    # for i in ndp:
    #     print(i)
    if sum(ns)==kk:
        print((ndp[keta][kk]+n)%mod)
    else:
        print((ndp[keta][kk])%mod)


    
