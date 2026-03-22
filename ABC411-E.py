from collections import defaultdict
n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
mod=998244353
nums=set()
numidx=defaultdict(list)
for i in range(n):
    for k in range(6):
        num=A[i][k]
        nums.add(num)
        numidx[num].append(i)
nums=list(nums)
#print(numidx)
nums.sort()
#print(nums)
b=[0]*(n)
#print(b)
count=0
for i in range(len(nums)):
    tmp=nums[i]
    for k in numidx[tmp]:
        if b[k]==0:
            count+=1
        b[k]+=1
    if count==n:
        last=i
        break
ans=1
trueans=0
for i in range(n):
    ans=ans *b[i]* pow(6, mod-2, mod) % mod
#print(ans)
trueans+=ans*nums[last]
beforeans=ans
#print(b,last)
for i in range(last+1,len(nums)):
    tmp=nums[i]
    for k in numidx[tmp]:
        ans=ans *(b[k]+1)* pow(b[k], mod-2, mod) % mod
        b[k]+=1
    trueans+=(ans-beforeans)*nums[i]
    beforeans=ans
print(trueans%mod)
    


        
    
    
