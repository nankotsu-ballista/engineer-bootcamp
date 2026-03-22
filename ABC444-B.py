n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    i=str(i)
    num=list(i)
    tmp=0
    for j in num:
        tmp+=int(j)
    if tmp==k:
        ans+=1
print(ans)
        