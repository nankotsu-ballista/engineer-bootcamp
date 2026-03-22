from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict
n,m,k=map(int,input().split())
A=list(map(int,input().split()))
if m==1:
  print(*A)
  exit()
count=defaultdict(int)
nowlist=[]
S=SortedList([])
for i in range(m):
  S.add(A[i])
KS=SortedList([])
ans=0
anss=[]
for i in range(k):
  KS.add(S[0])
  ans+=S[0]
  S.pop(0)
anss.append(ans)
for i in range(n-m):
  hidari=A[i]
  migi=A[i+m]
  if KS[-1]<hidari:
    S.discard(hidari)
  else:
    ans-=hidari
    ans+=S[0]
    KS.discard(hidari)
    KS.add(S[0])
    S.pop(0)
  S.add(migi)
  if KS[-1]<S[0]:
    anss.append(ans)
    continue
  else:
    sento,matubi=S[0],KS[-1]
    ans+=S[0]
    ans-=KS[-1]
    S.pop(0)
    KS.pop(-1)
    S.add(matubi)
    KS.add(sento)
  anss.append(ans)
print(*anss)