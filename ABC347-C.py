n,a,b=map(int,input().split())
D=list(map(int,input().split()))
mods=[0]*n
mody=set()
for i in range(n):
    mods[i]=D[i]%(a+b)
    mody.add(mods[i])
#print(mods)
mody=list(mody)
rang=abs(max(mods)-min(mods)+1)
#print(rang)
mody.sort()
#print(mody)
ans=0
for i in range(1,len(mody)):
    ans=max(abs(mody[i]-mody[i-1]),ans)
ans=max(ans,mody[0]+a+b-mody[-1])
#print(ans-1)

if b<=ans-1:
    print("Yes")
else:
    print("No")