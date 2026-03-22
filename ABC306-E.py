from sortedcontainers import SortedList
from collections import defaultdict
n,k,q=map(int,input().split())
klist=SortedList([0]*k)
otherlist=SortedList([0]*(n-k))
simplelist=defaultdict(int)
ksum=0
othercount=defaultdict(int)
othercount[0]=n-k
kcount=defaultdict(int)
kcount[0]=k
for i in range(q):
  #print(klist)
  #print(otherlist)
  x,y=map(int,input().split())
  tmp=simplelist[x]
  if othercount[tmp]!=0:
    otherlist.remove(tmp)
    othercount[tmp]-=1
  else:
    klist.remove(tmp)
    ksum-=tmp
    kcount[tmp]-=1
    
  simplelist[x]=y
  otherlist.add(y)
  othercount[y]+=1
  while len(klist)<k:
    tl=otherlist[-1]
    klist.add(tl)
    ksum+=tl
    otherlist.remove(tl)
    othercount[tl]-=1
    kcount[tl]+=1
  if otherlist:
    while klist[0]<otherlist[-1]:
      ksum-=klist[0]
      ksum+=otherlist[-1]
      tmpk=klist[0]
      tmpo=otherlist[-1]
      otherlist.add(tmpk)
      othercount[tmpk]+=1
      klist.add(tmpo)
      kcount[tmpo]+=1
      otherlist.remove(tmpo)
      othercount[tmpo]-=1
      klist.remove(tmpk)
      kcount[tmpk]-=1
  print(ksum)
