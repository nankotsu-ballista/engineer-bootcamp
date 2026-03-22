n=int(input())
parent=[]
size=[1]*n
for i in range(n):
    parent.append(i)
#print(parent)
def find(x):
    x-=1
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
def union(a,b):
    a-=1
    b-=1
    pa,pb=find(a),find(b)
    if pa == pb: return False
    if size[pa]< size[pb]:
        pa,pb=pb,pa
    parent[pb]=pa
    size[pa] += size[pb]
    return True
for i in range(n-1):
    u,v=map(int,input().split())
    if u!=1:
        union(u,v)
print(n-max(size))
