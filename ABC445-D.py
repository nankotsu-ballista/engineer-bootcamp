from collections import deque
hh,ww,n=map(int,input().split())
hitems=[]
witems=[]
for i in range(n):
    h,w=map(int,input().split())
    hitems.append((h,w,i))
    witems.append((w,h,i))
hitems.sort()
hitems.reverse()
witems.sort()
witems.reverse()
for i in range(n):
    d,d1,d2=witems[i]
    witems[i]=d1,d,d2
position=[[] for _ in range(n+1)]
tatehaba=hh
yokohaba=ww
hqueue=deque()
wqueue=deque()
#print(tatehaba,yokohaba)
#print()
for i in hitems:
    hqueue.append(i)
for i in witems:
    wqueue.append(i)
#print(hqueue)
#print(wqueue)
usedidx=set()

while hqueue and wqueue:
    while hqueue:
        Hhwid,Hwwid,hidx=hqueue.popleft()
        if hidx not in usedidx:
            break
    while wqueue:
        Whwid,Wwwid,widx=wqueue.popleft()
        if widx not in usedidx:
            break
    if tatehaba==Hhwid:
        yokohaba-=Hwwid
        usedidx.add(hidx)
        wqueue.appendleft((Whwid,Wwwid,widx))
        position[hidx]=(1,yokohaba+1)
    elif yokohaba==Wwwid:
        tatehaba-=Whwid
        usedidx.add(widx)
        hqueue.appendleft((Hhwid,Hwwid,hidx))
        position[widx]=(tatehaba+1,1)
#print(position)
for i in range(n):
    pp,ll=position[i]
    print(pp,ll)
