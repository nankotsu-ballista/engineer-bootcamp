from collections import deque
n=int(input())
A=list(map(int,input().split()))
q=int(input())
# before=[0]*(n+q+1)
# after=[0]*(n+q+1)
before={}
after={}
# print(before)
# print(after)
if n!=1:
    for i in range(len(A)):
        if i==0:
            after[A[i]]=A[i+1]
            before[A[i]]=-1
            continue
        if i==n-1:
            before[A[i]]=A[i-1]
            after[A[i]]=-5
            continue
        before[A[i]]=A[i-1]
        after[A[i]]=A[i+1]
else:
    before[A[0]]=-1
    after[A[0]]=-5
    



for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        if 2==1:
        #if before[x]==-1 and after[x]==-5:
            after[y]=-5
            after[x]=y
            before[y]=x
        else:
            x=Q[1]
            y=Q[2]
            after[y]=after.get(x, -5)
            if after.get(x, -5)!=-5:
                before[after[x]]=y
            after[x]=y
            before[y]=x
    if Q[0]==2:
        x=Q[1]
        if before.get(x, 0)!=-1:
            if before.get(x, 0) in after:
                after[before[x]]=after.get(x, -5)
        if after.get(x, -5)!=-5:
            if after.get(x) in before:
                before[after[x]]=before.get(x, 0)
        after[x]=0
        before[x]=0
    #print(before)
for k, v in before.items():
    if v==-1:
        start=k
        break
#print(start)
ans=[]
nxt=start
while nxt!=-5:
    ans.append(nxt)
    nxt=after.get(nxt, -5)
print(*ans)
