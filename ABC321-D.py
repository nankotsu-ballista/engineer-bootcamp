import bisect
n,m,p=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
ruiseki=[]
sum=0
ruiseki.append(0)
for i in range(m):
    sum+=B[i]
    ruiseki.append(sum)
ans=0

for i in range(n):
    t=bisect.bisect_left(B,p-A[i])
    ans+=A[i]*t+ruiseki[t]+p*(m-t)
    #print(A[i]*t+ruiseki[t]+p*(m-t))
print(ans)
    
    
    