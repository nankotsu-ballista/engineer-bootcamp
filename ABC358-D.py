n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
i=0
j=0
ans=0
while i<n and j<m:
    if B[j]<=A[i]:
        ans+=A[i]
        i+=1
        j+=1
    else:
        i+=1
if j==m:
    print(ans)
else:
    print(-1)
