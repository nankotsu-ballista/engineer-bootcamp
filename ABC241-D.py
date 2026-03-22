from sortedcontainers import SortedList
q=int(input())
s=SortedList([])
for _ in range(q):
  #print(s)
  que=list(map(int,input().split()))
  if que[0]==1:
      s.add(que[1])
  elif que[0]==2:
      idx=s.bisect_right(que[1])
      #print("idx",idx)
      if idx<que[2]:
          print(-1)
      else:
          print(s[idx-que[2]])
  elif que[0]==3:
    idx=s.bisect_left(que[1])
    #print("idx",idx)
    if idx+que[2]>len(s):
        print(-1)
    else:
        print(s[idx+que[2]-1])