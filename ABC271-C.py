from collections import deque,defaultdict
n=int(input())
A=list(map(int,input().split()))
A.sort()
q=deque()
amari=[]
for i in range(len(A)-1,0,-1):
    #print(i)
    if A[i]==A[i-1]:
        amari.append(A[i])
        A[i]=-1
#print(amari)
for i in A:
    if i==-1:
        continue
    q.append(i)
for i in amari:
    q.append(i)
page=1
while q:
    #print(q,page)
    idx=q.popleft()
    if idx==page:
        page+=1
    elif idx<page:
        q.append(10**10)
    elif idx>page:
        if len(q)>=2:
            q.pop()
            q.pop()
            page+=1
            q.appendleft(idx)
        else:
            q.appendleft(idx)
            break
if len(q)==2:
    page+=1
print(page-1)
            
        