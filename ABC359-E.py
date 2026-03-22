from collections import deque
n=int(input())
H=list(map(int,input().split()))
q=deque()
q.append((-1,-1))
time=0
times=[-1]*(n+2)
ans=[]
for i in range(n):
    nowidx=i
    nowhigh=H[i]
    while q:
        leftidx,lefthigh=q.pop()
        if lefthigh>=nowhigh:
            break
    if leftidx==-1:
        q.append((-1,-1))
        time=nowhigh*(nowidx+1)+1
        ans.append(time)
        times[nowidx]=time
    else:
        q.append((leftidx,lefthigh))
        time=times[leftidx]+(nowidx-leftidx)*nowhigh
        ans.append(time)
        times[nowidx]=time
    q.append((nowidx,nowhigh))
print(*ans)