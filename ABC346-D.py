n=int(input())
s=input()
c=list(map(int,input().split()))
ozcost=[0]*n
zocost=[0]*n
num="0"
sum=0
for i in range(n):
    if s[i]==num:
        t=0
    else:
        sum+=c[i]
    ozcost[i]=sum
    if num == "1":
        num="0"
    else:
        num="1"
num="1"
sum=0
for i in range(n):
    if s[i]==num:
        t=0
    else:
        sum+=c[i]
    zocost[i]=sum
    if num == "1":
        num="0"
    else:
        num="1"
ans=10**18
for i in range(1,n):
    q=ozcost[i-1]-zocost[i-1]+zocost[n-1]
    ans=min(ans,q)
for i in range(1,n):
    q=zocost[i-1]-ozcost[i-1]+ozcost[n-1]
    ans=min(ans,q)
print(ans)












