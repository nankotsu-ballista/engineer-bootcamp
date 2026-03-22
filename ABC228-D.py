from sortedcontainers import SortedList
q=int(input())
s=SortedList([])
reallist=[]
for i in range(2**20):
  s.add(i)
  reallist.append(-1)
#print(s)
for i in range(q):
    t,x=map(int,input().split())
    if t==1:
      idx=x%2**20
      if idx in s:
        s.remove(idx)
        reallist[idx]=x
      else:
        #print(s[s.bisect_left(idx)])
        if s.bisect_left(idx)!=len(s):
          reallist[s[s.bisect_left(idx)]]=x
          s.remove(s[s.bisect_left(idx)])
        else:
          reallist[s[0]]=x
          s.remove(s[0])
    elif t==2:
      print(reallist[x%2**20])
