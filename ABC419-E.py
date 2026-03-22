n,m,l=map(int,input().split())
A=list(map(int,input().split()))
dp=[[0]*(l) for _ in range(m)]
for i in range(n):
    A[i]=A[i]%m
for j in range(l):
    for i in range(m):
        for k in range((n//l)+1):
            if l*k+j>=n:
                continue
            dp[i][j]+=((m+i-A[l*k+j])%m)
# for i in dp:
#     print(i)
fdp=[[10000000]*(l+1) for _ in range(m)]
fdp[0][0]=0
for k in range(l):
    for i in range(m):
        for j in range(m):
            fdp[(i+j)%m][k+1]=min(fdp[(i+j)%m][k+1],fdp[i][k]+dp[j][k])
# for i in fdp:
#     print(i)
print(fdp[0][l])