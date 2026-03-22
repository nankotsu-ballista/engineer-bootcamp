n,m=map(int,input().split())
d=[0]*m
for i in range(n):
    l,r=map(int,input().split())
    d[r-1]=max(d[r-1],l)
#print(d)
for i in range(0,m-1):
    d[i+1]=max(d[i],d[i+1])
#print(d)
ans=0
for i in range(m):
    ans+=i-d[i]+1
print(ans)