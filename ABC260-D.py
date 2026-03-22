from collections import deque
from sortedcontainers import SortedList
banocard = SortedList([])
import bisect
n,k=map(int,input().split())
P=list(map(int,input().split()))
sokonum=[0]*(n+1)
sokonocard=[-1]*(n+1)
cards=[[]for _ in range(n+1)]
eatentime=[-1]*(n+1)
onespecial=[-1]*(n+1)

if k==1:
  for i in range(n):
    onespecial[P[i]]=i+1
  for i in range(1,n+1):
    print(onespecial[i])

  exit()
for i in range(n):
    idx=banocard.bisect_right(P[i])
    #print(idx)
    if idx==len(banocard):
      banocard.add(P[i])
      sokonum[idx+1]+=1
      sokonocard[P[i]]=P[i]
      cards[P[i]].append(P[i])
    else:
      soko=sokonocard[banocard[idx]]
      banocard.remove(banocard[idx])
      banocard.add(P[i])
      sokonocard[P[i]]=soko
      cards[soko].append(P[i])
      if len(cards[soko])==k:
        banocard.remove(P[i])
        for kk in cards[soko]:
          eatentime[kk]=i+1
        
    #print(cards[:7])
    #print(sokonocard[:7])
    #print(banocard)
#print(eatentime)
for i in range(1,n+1):
  print(eatentime[i])
    