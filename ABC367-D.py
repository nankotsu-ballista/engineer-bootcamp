N,M=map(int,input().split())
A=list(map(int,input().split()))
A=A+A
#print(A)
count=[0]*M
mods=[0]*(2*N)
sum=0
for i in range(2*N):
    sum+=A[i]
    sum=sum%M
    mods[i]=sum%M
#print(mods)
ans=0
for i in range(N-1):
    count[mods[i]]+=1
c=0
k=0
for i in range(N,2*N):
    # print(c)
    # print(count)
    ans+=count[c]
    c=mods[k]
    count[mods[k]]-=1
    count[mods[k+N-1]]+=1
    k+=1
print(ans)
    
    
