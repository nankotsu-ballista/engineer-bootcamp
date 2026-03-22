from collections import defaultdict,deque
import bisect
n,l,r=map(int,input().split())
count=defaultdict(int)
#rcount=defaultdict(int)

S=list(input())
ans=0
for i in range(n):
    if i-l>=0:
        count[S[i-l]]+=1
    if i-r-1>=0:
        count[S[i-r-1]]-=1
    ans+=count[S[i]]
    #print(i,count)
print(ans)