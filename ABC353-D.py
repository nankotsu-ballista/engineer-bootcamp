from collections import defaultdict
cnt = defaultdict(int)
n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
sums=[0]*20
q=[]
number=[[0]*20 for _ in range(n+1)]
for i in range(n):
    l=len(str(a[i]))
    sums[l]+=1
    q.append(sums.copy())
q=q[:n-1]
ls=[]
for i in q:
    total=0
    for j in range(20):
        total+=10**j*i[j]
    ls.append(total)
ls=ls[::-1]
ans=0
ruiseki=[]
a=a[::-1]
total=0
for i in a:
    total+=i
    ruiseki.append(total)
for i in range(n-1):
    ans+=a[i]*ls[i]%998244353
    ans+=ruiseki[-1]-ruiseki[i]%998244353
print(ans%998244353)
        
