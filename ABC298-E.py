n,a,b,p,q=map(int,input().split())
MOD = 998244353
dpT = [[0]*(n+1) for _ in range(n+1)]
dpA = [[0]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dpT[n][i]=1
    dpA[n][i]=1
for i in range(n):
    dpT[i][n] = 0
    dpA[i][n] = 0

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        tmp=0
        for k in range(1,p+1):
            tmp+=dpA[min(i+k,n)][j]
        dpT[i][j]=tmp*pow(p, MOD-2, MOD) % MOD
        tmp=0
        for k in range(1,q+1):
            tmp+=dpT[i][min(j+k,n)]
        dpA[i][j]=tmp*pow(q, MOD-2, MOD) % MOD
print(dpT[a][b])
    
    