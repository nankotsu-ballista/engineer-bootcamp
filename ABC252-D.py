from collections import deque,defaultdict
n=int(input())
numidxs=[[]for _ in range(2*10**5+1)]
A=list(map(int,input().split()))
for i in range(n):
    numidxs[A[i]].append(i)
#print(numidxs)
sum=0
for idxs in numidxs:
    if len(idxs)>=2:
        sum+=(len(idxs)*(len(idxs)-1))//2*(n-len(idxs))
    if len(idxs)>=3:
        sum+=(len(idxs)*(len(idxs)-1)*(len(idxs)-2))//6
#print(sum)
print(n*(n-1)*(n-2)//6-sum)
            
            
    