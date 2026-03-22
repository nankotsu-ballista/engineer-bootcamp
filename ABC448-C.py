from sortedcontainers import SortedSet, SortedList, SortedDict
n,q=map(int,input().split())
A=list(map(int,input().split()))
S = SortedList([])
for i in A:
  S.add(i)
for i in range(q):
    k=int(input())
    B=list(map(int,input().split()))
    for i in range(k):
      S.discard(A[B[i]-1])
    print(S[0])
    for i in range(k):
      S.add(A[B[i]-1])
    