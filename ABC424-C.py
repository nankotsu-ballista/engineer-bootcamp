from collections import deque
n=int(input())
skill=[[]for _ in range(n+1)]
check=[False]*(n+1)
for i in range(n):
    a,b=map(int,input().split())
    if a==0 and b==0:
        check[i+1]=True
    else:
        skill[a].append(i+1)
        skill[b].append(i+1)
q=deque()
for i in range(n+1):
    if check[i]==True:
        q.append(i)
# print(q)
while q:
    t=q.pop()
    for k in skill[t]:
        if check[k]==False:
            q.append(k)
            check[k]=True
# print(skill)
# print(check)
ans=0
for i in range(n+1):
    if check[i]==True:
        ans+=1
print(ans)
