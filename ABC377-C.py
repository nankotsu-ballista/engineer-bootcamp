from collections import defaultdict
n,m=map(int,input().split())
index=set()
for i in range(m):
    a,b=map(int,input().split())
    index.add((a+2,b+1))
    index.add((a+2,b-1))
    index.add((a+1,b+2))
    index.add((a+1,b-2))
    index.add((a-2,b+1))
    index.add((a-2,b-1))
    index.add((a-1,b+2))
    index.add((a-1,b-2))
    index.add((a,b))
index=list(index)
#print(index)
count=0
for j in range(len(index)):
    if index[j][0] >= 1 and index[j][0] <= n and index[j][1] <= n and index[j][1] >= 1:
        count+=1
#print(count)
print(n**2-count)
    
    
