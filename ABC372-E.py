n,q=map(int,input().split())
parents=[]
sizes=[]
for i in range(n+1):
    parents.append(i)
    sizes.append(1)
members=[[] for _ in range(n+1)]
for i in range(n+1):
    members[i].append(i)
#print(members)
def find(a):
    if parents[a]== a:
        return a
    else:
        parents[a]=find(parents[a])
        return parents[a]
def union(a,b):
    ra=find(a)
    rb=find(b)
    if ra == rb:
        return False
    else:
        if sizes[ra]<sizes[rb]:
            ra,rb=rb,ra
        sizes[ra]+=sizes[rb]
        parents[rb]=ra
        members[ra]=members[ra]+members[rb]
        members[ra].sort()
        members[rb] = []
        if len(members[ra])>10:
            members[ra]=members[ra][-10:]
        return True
    
for i in range(q):
    num,q1,q2=map(int,input().split())
    if num == 1:
        union(q1,q2)
    elif num == 2:
        rr=find(q1)
        if len(members[rr])<q2:
            print(-1)
        else:
            print(members[rr][-q2])
#print(sizes)
# print(members)