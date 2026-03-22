import bisect
from collections import defaultdict
n,m,c=map(int,input().split())
A=list(map(int,input().split()))
sum=0
player=defaultdict(int)
for a in A:
    player[a]+=1
#print(player)
players=defaultdict(int)
hitopoji=[]
for r, num in player.items():
    hitopoji.append((r,num))
hitopoji.sort()
#print(hitopoji)
sun=0
for r, num in hitopoji:
    sun+=num
    players[r]=(sun)
sum=0
ruiseki=[0]
poji=[]
for i,j in hitopoji:
    sum+=j
    ruiseki.append(sum)
    poji.append(i)
for i,j in hitopoji:
    sum+=j
    ruiseki.append(sum)
#print(ruiseki)
#print(poji)
humancount=ruiseki[0]
ans=0
#print(hitopoji)
butter=[0] 
for i,k in hitopoji:
    butter.append(i)
butter.append(m)
#print(butter)
shouldsearch=[]
for i in range(len(butter)-1):
    shouldsearch.append((butter[i],butter[i+1]-butter[i]))
#print(shouldsearch)
for i,k in shouldsearch:
    idx = bisect.bisect_left(poji, i+0.5) - 1
    if idx<0:
        humancount = 0
    else:
        humancount=players[poji[idx]]
    #print(humancount)
    l=bisect.bisect_left(ruiseki,humancount)
    r=bisect.bisect_left(ruiseki,humancount+c)
    #print("ans",ruiseki[r]-ruiseki[l])
    ans+=k*(ruiseki[r]-ruiseki[l])
print(ans)
    
    
    
    
    
    
    
    
    
    
    