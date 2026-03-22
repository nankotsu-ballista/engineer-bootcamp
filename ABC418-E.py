from collections import defaultdict
import math
katamuki=defaultdict(int)
sihenkei=defaultdict(int)
n=int(input())
items=[]
for i in range(n):
    x,y=map(int,input().split())
    items.append((x,y))
for i in range(n-1):
    for k in range(i+1,n):
        x1,y1=items[i]
        x2,y2=items[k]
        sihenkei[(x1+x2),(y1+y2)]+=1
        if x1<x2:
            x1,y1,x2,y2=x2,y2,x1,y1
        bunbo=(x1-x2)
        bunsi=(y1-y2)
        if bunbo!=0 and bunsi==0:
            bunbo=1
        elif bunbo==0 and bunsi!=0:
            bunsi=1
        gc=math.gcd(bunbo,bunsi)
        katamuki[(bunbo//gc,bunsi//gc)]+=1
ans = 0
# print(katamuki)
# print(sihenkei)
for i in sihenkei.values():
    ans-=i*(i-1)//2
for i in katamuki.values():
    ans+=i*(i-1)//2
print(ans)