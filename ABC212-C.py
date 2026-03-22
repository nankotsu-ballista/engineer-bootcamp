import bisect
n,m=map(int,input().split())
A=list(map(int,(input().split())))
B=list(map(int,(input().split())))
A.sort()
B.sort()
ans=10**18
for i in range(m):
    tmp=B[i]
    #print(bisect.bisect_left(A,tmp))
    q=bisect.bisect_left(A,tmp)
    if q!=0:
        ans=min(ans,abs(tmp-A[q-1]))
    if q==n-1:
        ans=min(ans,abs(tmp-A[q]))
    if q<n-1:
        ans=min(ans,abs(tmp-A[q+1]))
        ans=min(ans,abs(tmp-A[q]))
print(ans)