import heapq
from collections import deque
q=int(input())
hq=[]
qq=deque()
for i in range(q):
    # print("hq",hq)
    # print("qq",qq)
    que=list(map(int,input().split()))
    if que[0]==1:
      qq.append(que[1])
    elif que[0]==2:
      if hq:
        a=heapq.heappop(hq)
      else:
        a=qq.popleft()
      print(a)
    elif que[0]==3:
        for k in range(len(qq)):
            i=qq.popleft()
            heapq.heappush(hq,i)