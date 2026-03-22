from collections import deque
n=int(input())
A=list(map(int,input().split()))
nyujisu=[0]*(n+1)
for i in range(n):
    nyujisu[A[i]]+=1
A=[0]+A
#print(nyujisu)
q=deque()
for i in range(1,n+1):
    if nyujisu[i]==0:
        q.append(i)
#print(q)
while q:
    idx=q.popleft()
    nyujisu[A[idx]]-=1
    if nyujisu[A[idx]]==0:
        q.append(A[idx])
#print(nyujisu)
print(sum(nyujisu))
