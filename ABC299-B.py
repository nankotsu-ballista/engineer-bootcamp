n,t=map(int,input().split())
c=list(map(int,input().split()))
r=list(map(int,input().split()))
itti=-1
other=-1
ittiidx=-1
otheridx=-1
for i in range(n):
    if c[i]==t:
        if itti<r[i]:
            ittiidx=i
            itti=r[i]
    if c[i]==c[0]:
        if other<r[i]:
            otheridx=i
            other=r[i]
if ittiidx==-1:
    print(otheridx+1)
else:
    print(ittiidx+1)
        