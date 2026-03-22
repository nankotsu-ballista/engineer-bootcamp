n,m=map(int,input().split())
x=list(map(int,input().split()))
for i in range(m):
    x[i]-=1
bridge=[]
imos=[0]*(n)
#print(imos)
for i in range(m-1):
    t=abs(x[i+1]-x[i])
    l=min(x[i+1],x[i])
    r=max(x[i+1],x[i])
    if r-l<l+n-r:
        imos[l]+=abs(n-t-t)
        imos[r]-=abs(n-t-t)
    else:
        imos[0]+=abs(n-t-t)
        imos[r]+=abs(n-t-t)
        imos[l]-=abs(n-t-t)
    #print(t,l,r,abs(n-t-t))
#print(imos)
#print(bridge)
sum=0
for k in imos:
    sum+=k
    bridge.append(sum)
#print(bridge)
ans=0
for i in range(m-1):
    t=abs(x[i+1]-x[i])
    l=min(x[i+1],x[i])
    r=max(x[i+1],x[i])
    ans+=min(abs(r-l),abs(l+n-r))
    #print(r,l)
print(ans+min(bridge))
#print(bridge)