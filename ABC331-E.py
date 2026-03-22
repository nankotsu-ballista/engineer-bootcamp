from collections import defaultdict
n,m,l=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
B=[]
for i in range(m):
    B.append((b[i],i))
    
s=defaultdict(set)
for _ in range(l):
    c,d=map(int,input().split())
    s[c-1].add(d-1)
B.sort()
B.reverse()
#print(s)
#print(B)
ans=0
for i in range(n):
    for k in range(m):
        value,idx=B[k]
        if idx not in s[i]:
            ans=max(ans,value+a[i])
            break

print(ans)