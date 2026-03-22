n,q=map(int,input().split())
C=list(map(int,input().split()))
box=[set() for _ in range(n+1)]
for i in range(n):
    box[i+1].add(C[i])
#print(box)
for i in range(q):
    #print(box)
    a,b=map(int,input().split())
    if len(box[a])<len(box[b]):
        for k in box[a]:
            box[b].add(k)
        box[a]=set()
        print(len(box[b]))
    else:
        for k in box[b]:
            box[a].add(k)
        box[b]=set()
        box[a],box[b]=box[b],box[a]
        print(len(box[b]))
    
    