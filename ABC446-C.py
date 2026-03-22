from collections import deque
t=int(input())
for _ in range(t):
    n,d=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    q=deque()
    eggcount=0
    for i in range(n):
        q.append((i,A[i]))
        eggcount+=A[i]
        eggcount-=B[i]
        needegg=B[i]
        while needegg>0:
            day,egg=q.popleft()
            if needegg<egg:
                egg=egg-needegg
                needegg=0
                q.appendleft((day,egg))
                break
            else:
                needegg=needegg-egg
        while q:
            day,egg=q.popleft()
            if i-day<d:
                q.appendleft((day,egg))
                break
            else:
                eggcount-=egg
    print(eggcount)
            
    
        
        
    
    