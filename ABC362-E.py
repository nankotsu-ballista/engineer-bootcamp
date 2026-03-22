n=int(input())
A=list(map(int,input().split()))
dp=[[[0]*(n+1)for _ in range(n+1)]for _ in range(n+1)]

for i in range(n):
    for k in range(i+1,n):
        dp[i][k][2]=1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if k<2:
                continue
            diff=(A[j]-A[i])//(k-1)
            if (A[j]-A[i])%(k-1)!= 0:
                continue
            for nxt in range(j+1,n):
                if diff==A[nxt]-A[j]:
                    dp[i][nxt][k+1]+=dp[i][j][k]
                    dp[i][nxt][k+1]=dp[i][nxt][k+1]%998244353
anss=[0]*(n+1)
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            anss[k]+=dp[i][j][k]
anss[1]=n
for i in range(n+1):
    anss[i]=anss[i]%998244353
print(*anss[1:])
            
            
            
            
            
            
            
            
            
            
            
            