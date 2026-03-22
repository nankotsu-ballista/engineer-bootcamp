n,d=map(int,input().split())
A=list(map(int,input().split()))
T=[0]*(10**6+1)
anss=0
if d==0:
    Count=[0]*(10**6+1)
    for l in A:
        Count[l]+=1
    for c in Count:
        if c!=0:
            anss+=1
    print(n-anss)
    exit()
for i in A:
    T[i]+=1
C=[[] for _ in range(d)]
for i in range(len(T)):
    C[i%d].append(T[i])
    

ans=0
for c in C:
    dp=[[0]*2 for _ in range(len(c)+1)]
    for t in range(len(c)):
        dp[t+1][0] = max(dp[t][0], dp[t][1])
        dp[t+1][1]=dp[t][0]+c[t]
    #print(dp)
    ans+=max(dp[len(c)][0],dp[len(c)][1])
print(n-ans)
        
        