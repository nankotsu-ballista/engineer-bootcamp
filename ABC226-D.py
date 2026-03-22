from functools import lru_cache
import math
n=int(input())
points=[]
s=set()
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
for i in range(n-1):
    for k in range(i+1,n):
        xdiff=points[k][0]-points[i][0]
        ydiff=points[k][1]-points[i][1]
        yaku=math.gcd(xdiff,ydiff)
        s.add((xdiff//yaku,ydiff//yaku))
        s.add((-xdiff//yaku,-ydiff//yaku))
#print(s)
print(len(s))