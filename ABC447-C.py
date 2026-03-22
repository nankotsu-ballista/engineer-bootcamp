from collections import deque
s=list(input())
t=list(input())
slist=deque()
tlist=deque()
for i in s:
    slist.append(i)
for i in t:
    tlist.append(i)
#print(slist)
#print(tlist)
possiblecheck=True
cost=0
while slist or tlist:
    sval=""
    tval=""
    if slist:
        sval=slist.popleft()
    if tlist:
        tval=tlist.popleft()
    #print(sval,tval)
    if sval==tval:
        continue
    if sval=="A":
        cost+=1
        tlist.appendleft(tval)
        continue
    if tval=="A":
        cost+=1
        slist.appendleft(sval)
        continue
    
    if tval!=sval:
        print(-1)
        exit()
print(cost)
    
    

        
    