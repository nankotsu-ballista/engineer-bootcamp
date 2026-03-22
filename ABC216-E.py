import heapq
from collections import deque
import bisect
n,k=map(int,input().split())
A=list(map(int,input().split()))
ans=0
if sum(A)<=k:
    for i in range(len(A)):
        ans+=((A[i]+1)*A[i])//2
    print(ans)
    exit()
A.sort()
A.reverse()
A=A+[0]
sums=[]
sum=A[0]
#print(A)
for i in range(1,n+1):
    sum+=A[i]
    sums.append(sum-A[i]*(i+1))
#print(sums)
num=k
idx=bisect.bisect_left(sums,num)
#print(idx)
A=A[:idx+1]
#print(A)
tmp=A[-1]
ans=0
for i in range(len(A)):
    ans+=((A[i]-tmp)*(A[i]+tmp+1))//2
    num-=(A[i]-tmp)
    A[i]=tmp
#print(num)
#print(ans)
amari=num%len(A)
shou=num//len(A)
#print(shou)
#print((shou)*len(A)*((tmp+tmp-shou+1))//2)
t=((shou)*len(A)*((tmp+tmp-shou+1))//2)
#print(amari*(tmp-shou))
tt=(amari*(tmp-shou))
#print(A)
print(ans+t+tt)
    
    