from sortedcontainers import SortedSet

import bisect
n,q=map(int,input().split())
blacks=SortedSet([])
ans=n
black_len=0
for _ in range(q):
    l,r=map(int,input().split())
    i= blacks.bisect_left((l,-10**18))
    if i>0 and blacks[i-1][1] >=l-1:
        i-=1
    nl,nr = l,r
    while i < len(blacks) and blacks[i][0] <= nr+1:
        a,b=blacks[i]
        black_len -=(b-a+1)
        nl=min(nl,a)
        nr = max(nr,b)
        blacks.pop(i)
    blacks.add((nl,nr))
    black_len+=(nr - nl + 1)
    ans = n - black_len
    print(ans)
    
    
    
    
    
    
    
    
    
    
        