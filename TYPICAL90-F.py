from collections import deque
import heapq
hq=[]
n,k=map(int,input().split())
s=input()
s=list(s)
ans=[]
nxt_pos=0
for i in range(n):
    heapq.heappush(hq,(s[i],i))
    if n<=i+k:
        while True:
            moji,idx=heapq.heappop(hq)
            if idx>=nxt_pos:
                ans.append(moji)
                nxt_pos = idx + 1
                break
print("".join(ans))