from collections import deque
s=input()
if s =="atcoder":
    print(0)
    exit()
se=set()
se.add(s)
s=list(s)
q=deque()
q.append((s,0))

while q:
    S,time=q.popleft()
    for i in range(6):
        S[i+1],S[i]=S[i],S[i+1]
        for k in range(8):
            tmp=""
            for t in range(7):
                tmp=tmp+S[t]
            if tmp=="atcoder":
                print(time+1)
                exit()
            if tmp not in se:
                se.add(tmp)
                q.append((S[:],time+1))
        S[i],S[i+1]=S[i+1],S[i]
        
        
        