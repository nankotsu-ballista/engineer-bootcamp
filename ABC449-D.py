l,r,d,u=map(int,input().split())
ans=0
for i in range(10**6+2,-1,-1):
    dx=max(0,min(i,r)-max(-i,l)+1)
    dy=max(0,min(i,u)-max(-i,d)+1)
    if i%2==0:
        ans+=dx*dy
    else:
        ans-=dx*dy
print(ans)