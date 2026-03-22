from itertools import combinations
N=int(input())
INF=10**12
dp=[-INF]*(2**N)
dp[0]=0
tq=[]
for i in range(N-1):
    c=list(map(int,input().split()))
    tq.append(c)
    
for bit in range(1<<N):
    t=[]
    for k in range(N):
        t.append(k)
    for i in range(N):
        if bit>>i & 1:
            t.remove(i)
    if N%2==0:
        if len(t)%2==1:
            continue
    #print(t)
    for c in combinations(t, 2):
        # print(c)
        # print(dp[bit+2**c[0]+2**c[1]],dp[bit]+tq[c[0]][c[1]-c[0]-1])
        # print(bit,bit+2**c[0]+2**c[1])
        # print(tq[c[0]][c[1]-c[0]-1])
        dp[bit+2**c[0]+2**c[1]]=max(dp[bit+2**c[0]+2**c[1]],dp[bit]+tq[c[0]][c[1]-c[0]-1])
if N%2==0:
    print(dp[-1])
    exit()
ans=0
for i in range(N):
    ans=max(ans,dp[2**N-1-(2**i)])
print(ans)
    

        
    
            