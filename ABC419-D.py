n,m=map(int,input().split())
s=input()
t=input()
hairetu=[0]*n
forans=[0]*n
for i in range(m):
    l,r=map(int,input().split())
    hairetu[l-1]+=1
    if r==n:
        continue
    else:
        hairetu[r]-=1
#print(hairetu)
summ=0
for i in range(n):
    summ+=hairetu[i]
    if summ%2==1:
        forans[i]=1
    else:
        forans[i]=0
#print(forans)
s=list(s)
t=list(t)
for i in range(n):
    if forans[i]==1:
        s[i]=t[i]
#print(s)
ans = "".join(s)
print(ans)
