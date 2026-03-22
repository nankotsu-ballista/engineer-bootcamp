n=int(input())
a=list(map(int,input().split()))
r=n//2+1
l=0
while l+1<r:
    mid=(l+r)//2
    lowers=a[n-mid:n]
    uppers=a[:mid]
    check=True
    for i in range(mid):
        if lowers[i]>=uppers[i]*2:
            continue
        else:
            check=False
            break
    if check==True:
        l=mid
    else:
        r=mid
    #print(l,r)
print(l)