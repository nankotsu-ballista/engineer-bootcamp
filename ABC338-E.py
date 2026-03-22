import heapq
from collections import deque
n=int(input())
items=[]
for i in range(n):
    a,b=map(int,input().split())
    if b<a:
        a,b=b,a
    items.append((a,b))
items.sort()
#print(items)
circle=[-1]*(4*10**5+1)
s=set()
stack=deque()
for i in range(n):
    a,b=items[i]
    circle[a]=i
    circle[b]=i
    
#print(circle[:10])
for i in range(1,4*10**5):
    if circle[i]==-1:
        continue
    else:
        if circle[i] not in s:
            stack.append(circle[i])
            s.add(circle[i])
        else:
            t=stack.pop()
            if t != circle[i]:
                print("Yes")
                exit()
print("No")

        
    

    