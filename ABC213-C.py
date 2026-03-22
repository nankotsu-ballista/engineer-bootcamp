from collections import defaultdict
h,w,n=map(int,input().split())
A=set()
B=set()
items=[]
AA=defaultdict(list)
BB=defaultdict(list)
for i in range(n):
    a,b=map(int,input().split())
    A.add(a)
    B.add(b)
    items.append((a,b))
A=list(A)
B=list(B)
A.sort()
B.sort()
idx=1
for i in A:
    AA[i]=idx
    idx+=1
idx=1
for i in B:
    BB[i]=idx
    idx+=1
# print(AA)
# print(BB)
for i in range(n):
    a,b=items[i]
    print(AA[a],BB[b])
