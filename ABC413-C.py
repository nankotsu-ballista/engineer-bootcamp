from collections import deque
import sys
Q = int(input())
A=deque()
ans=[]

for _ in range(Q):
    query = input().split()
    
    if query[0] == '1':
      c = int(query[1])
      x = int(query[2])
      A.append((x,c))
    else:
      k = int(query[1])
      total = 0
      while k > 0:
        val,cnt = A[0]
        if cnt <= k:
          total += val * cnt
          A.popleft()
          k -= cnt
        else:
          total+= val * k
          A[0] = (val, cnt - k)
          k = 0
      ans.append(str(total))
print('\n'.join(ans))            
