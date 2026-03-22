n,k=map(int,input().split())
A=list(map(int,input().split()))
for i in range(n):
    A[i]=A[i]%k
A.sort()
#print(A)
matubi=A[-1]
ans=10**18
for i in range(n):
    ans=min(ans,matubi-A[i])
    matubi=A[i]+k
print(ans)