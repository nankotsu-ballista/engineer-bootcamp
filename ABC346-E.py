from collections import deque
h,w,m=map(int,input().split())
q=[]
for i in range(m):
    t,a,x=map(int,input().split())
    q.append((t,a,x))
q.reverse()
tate=set()
yoko=set()
color=set()
for i in range(h):
    tate.add(i+1)
for i in range(w):
    yoko.add(i+1)
tatecount=0
yokocount=0
zerocheck=False
colorcounter=[0]*(2*10**5+1)
for i in range(m):
    t,a,x=q[i]
    if t==1 and yokocount!=w:
        if a in tate:
            tate.discard(a)
            colorcounter[x]+=w-yokocount
            tatecount+=1
    elif t==2 and tatecount!=h:
        if a in yoko:
            yoko.discard(a)
            colorcounter[x]+=h-tatecount
            yokocount+=1
sum=0
anss=[]
for i in range((2*10**5+1)):
    sum+=colorcounter[i]
colorcounter[0]+=(h*w-sum)
for i in range((2*10**5+1)):
    if colorcounter[i]!=0:
        anss.append((i,colorcounter[i]))
print(len(anss))
for i in range(len(anss)):
    v,n=anss[i]
    print(v,n)


