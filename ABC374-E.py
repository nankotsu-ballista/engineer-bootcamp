n,x=map(int,input().split())
items=[]
for i in range(n):
    a,p,b,q=map(int,input().split())
    items.append((a,p,b,q))
r=10**18
l=0
while l<r:
    mid=(l+r)//2
    cost=x
    for i in range(n):
        tmp=10**18
        tmpans=[]
        a,p,b,q=items[i]
        for k in range(101):
            rest=max(0,mid-a*k)
            t=(rest+b-1)//b
            tmp=min(tmp, p*k+q*t)
        for k in range(101):
            rest = max(0,mid-b*k)
            t = (rest+a-1) // a
            tmp = min(tmp,q*k +p*t)
        cost-=tmp
    if cost<0:
        r=mid
    else:
        l=mid+1
print(l-1)