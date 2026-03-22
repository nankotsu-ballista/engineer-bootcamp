from collections import deque
import heapq
n=int(input())
uresisasum=0
hq=[]
bsum=0
wsum=0
dp=[0]*((500**2//2)+1)
items=[]
for i in range(n):
    w,h,b=map(int,input().split())
    items.append((w,h,b))
    wsum+=w

for i in range(n):
    w,h,b=items[i]
    bsum+=b
    value=h-b
    for i in range((wsum//2),-1,-1):
        if i-w>=0:
            dp[i]=max(dp[i-w]+value,dp[i])
print(max(dp)+bsum)
