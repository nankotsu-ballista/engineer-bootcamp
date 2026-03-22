n=int(input())
A=list(map(int,input().split()))
count=[[] for _ in range(n+1)]
for i in range(n):
    count[A[i]].append(i)
#print(count)
ans=0
for i in range(1,n+1):
    tmp=[-1]+count[i]+[n]
    #print(tmp)
    sum=n*(n+1)//2
    for k in range(len(tmp)-1):
        sum-=(tmp[k+1]-tmp[k]-1)*(tmp[k+1]-tmp[k])//2
    ans+=sum
    #print(ans)
        
print(ans)