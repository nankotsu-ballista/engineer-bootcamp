n,m,k=map(int,input().split())
t=[[]for _ in range(100)]
q=[]
for i in range(k):
    a,b=map(int,input().split())
    t[a].append(b)
    if len(t[a])==m:
        q.append(a)
#print(q)
if q:
    print(*q)