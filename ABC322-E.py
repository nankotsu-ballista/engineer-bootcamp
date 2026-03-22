n,k,p=map(int,input().split())
seq=[]
def goshin(c):
    seq=[]
    for i in range(k):
        seq.append(c%6)
        c//=6
    return seq
def modosu(c):
    sum=0
    for i in range(k):
        sum+=6**(i)*c[i]
    return sum
# print(goshin(27))
# print(modosu([2, 0, 1, 0]))
        
dp=[[10**18]*(6**k+1) for _ in range(n+1)]
    
dp[0][0]=0
for i in range(n):
    inp=list(map(int,input().split()))
    C=inp[0]
    A=inp[1:]
    for j in range(6**k):
        status=goshin(j)
        newstatus=[]
        for kp in range(k):
            newstatus.append(min(status[kp]+A[kp],5))
        dpidx=modosu(newstatus)
        #print(dpidx)
        dp[i+1][dpidx]=min(dp[i][dpidx],dp[i][j]+C,dp[i+1][dpidx])
        dp[i+1][j]=min(dp[i][j],dp[i+1][j])
ans=10**18
#print(k)
for ea in range(6**k+1):
    lists=goshin(ea)
    check=True
    for ka in lists:
        if ka<p:
            check=False
            break
    if check==True:
        ans=min(ans,dp[n][ea])
    #print(ea,check,lists)
if ans==10**18:
    print(-1)
else:
    print(ans)
    
        
        
        
            
        
        
    