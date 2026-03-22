n,q=map(int,input().split())
s=input()
idx=[0]*n
for i in range(n-1):
    if s[i]==s[i+1]:
        idx[i]+=1
#print(idx)
idxsum=[0]*n
count=0
for i in range(n):
    if idx[i]==1:
        count+=1
    idxsum[i]=count
#print(idxsum)
for i in range(q):
    l,r=map(int,input().split())
    ans=idxsum[r-1]-idxsum[l-1]
    if idx[r-1]==1:
         ans-=1
    if idx[l-1]==1:
         ans+=1
    print(ans)