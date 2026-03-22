import bisect
n=int(input())
items=[]
asums=[]
sum=0
for i in range(n):
    p,a,b=map(int,input().split())
    items.append((p,a,b))
    sum+=b
    asums.append(sum)
q=int(input())
dp=[[0]*1010 for _ in range(n+1)]
for c in range(1010):
    dp[n][c]=c
#print(items)
for i in range(n-1,-1,-1):
    #print(i)
    p,a,b=items[i]
    # sum+=b
    # asums.append(sum)
    for k in range(1009):
        if k<=p:
            dp[i][k]=dp[i+1][k+a]
        else:
            dp[i][k]=dp[i+1][max(k-b,0)]
for i in range(n+1):
    dps=dp[i]
    #print(dps[0:10])
#print(asums)
for i in range(q):
    x=int(input())
    if i >-1:
        if x>=1000:
            idx=bisect.bisect_left(asums,x-1000)
            #print(idx)
            if idx==n:
                print(x-asums[-1])
            else:
                c=(x-asums[idx])
                print(dp[idx+1][c])
        else:
            print(dp[0][x])

            
        
        

