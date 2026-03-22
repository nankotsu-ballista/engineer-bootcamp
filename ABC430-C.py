import bisect
n,a,b=map(int,input().split())
s=input()
asum=0
bsum=0
asums=[0]
bsums=[0]
for i in range(n):
    if s[i]=="a":
        asum+=1
    else:
        bsum+=1
    asums.append(asum)
    bsums.append(bsum)
# print(asums)
# print(bsums)
ans=0
for i in range(n+1):
    aidx=bisect.bisect_left(asums,asums[i]+a)
    bidx=bisect.bisect_left(bsums,bsums[i]+b)
    ans+=max(bidx-aidx,0)
print(ans)