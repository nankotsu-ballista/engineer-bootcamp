import bisect              
n,q=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
for _ in range(q):
    b,k=map(int,input().split())
    left=0
    right = 10**17
    while left<right:
        mid=(right+left)//2
        L=bisect.bisect_left(A,b-mid)
        R=bisect.bisect_right(A,b+mid)
        cnt=R-L
        if cnt<k:
            left=mid+1
        if cnt>=k:
            right=mid
    print(left)