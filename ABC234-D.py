from sortedcontainers import SortedList
n,k=map(int,input().split())
P=list(map(int,input().split()))
s=SortedList([])
for i in range(k):
  s.add(P[i])
print(s[-k])
for i in range(k,n):
  s.add(P[i])
  print(s[-k])
  
  