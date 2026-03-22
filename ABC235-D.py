from collections import defaultdict,deque
a,n=map(int,input().split())
q=deque()
s=set()
q.append((1,0))
count=0
while q:
    num,time=q.popleft()
    tmp=num*a
    if num==n:
        print(time)
        exit()
    if tmp not in s and tmp<10**6+1:
        s.add(tmp)
        q.append((tmp,time+1))
    if num%10!=0 and num>10:
        num=list(str(num))
        num=[num[-1]] + num[:-1]
        newnum=""
        for k in num:
            newnum=newnum+k
        newnum=int(newnum)
        if newnum not in s and newnum<10**6+1:
            q.append((newnum,time+1))
            s.add(newnum)
print(-1)