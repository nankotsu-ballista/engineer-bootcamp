from sortedcontainers import SortedList,SortedSet

n=int(input())
q=int(input())
boxes=[SortedList([]) for _ in range(2*10**5+1)]
cards=[SortedSet([]) for _ in range(2*10**5+1)]
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
      cards[query[1]].add(query[2])
      boxes[query[2]].add(query[1])
    elif query[0]==2:
      print(*boxes[query[1]])
    elif query[0]==3:
      print(*cards[query[1]])
    
    
            