from sortedcontainers import SortedList
l,q=map(int,input().split())
kireme = SortedList([0,l])
for i in range(q):
    c,x=map(int,input().split())
    if c==1:
        kireme.add(x)
    elif c==2:
      lef=(kireme.bisect_left(x+0.1)-1)
      rig=(kireme.bisect_right(x+0.1))
      print(kireme[rig]-kireme[lef])