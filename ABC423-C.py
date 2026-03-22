n,r=map(int,input().split())
L=list(map(int,input().split()))
mostLzero=-1
mostRzero=-1
for i in range(r):
    if L[i]==0:
        mostLzero=i
        break
for i in range(r,n):
    if L[i]==0:
        mostRzero=i
# print(mostRzero)
# print(mostLzero)
cnt=0
if mostLzero != -1:
    for i in range(mostLzero,r):
        if L[i]==0:
            cnt+=1
        elif L[i]==1:
            cnt+=2
if mostRzero != -1:
    for i in range(r,mostRzero+1):
        if L[i]==0:
            cnt+=1
        elif L[i]==1:
            cnt+=2

print(cnt)
        
