n,k=map(int,input().split())
l=0
r=10**8+5000
while r>l:
    mid=(r+l)//2
    if ((mid+1)*(2*n+mid))//2>=k:
        r=mid
    else:
        l=mid+1
print(l)