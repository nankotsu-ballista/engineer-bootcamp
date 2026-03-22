H,W=map(int,input().split())
points=[list(map(int,input().split())) for _ in range(H)]
if H==1 and W == 1:
    print(points[0][0])
    exit()
states ={0}
for i in range(H*W-1):
    ns=set()
    for t in states:
        ns.add(t)
        if i%W!=(W-1) and ((t >> i) & 1) == 0 and ((t >> (i + 1)) & 1) == 0:
            ns.add( t | (1 << i) | (1 << (i+1)) )
        if i//W!=(H-1) and i+W < H*W and ((t >> (i + W)) & 1) == 0 and ((t >> i) & 1) == 0:
            ns.add( t | (1 << i) | (1 << (i+W)) )
    states=ns
ans=0
for t in ns:
    now = 0
    for i in range(H):
        for k in range(W):
            bit = i*W+k
            if ((t >> bit) & 1) == 0:
                now ^= points[i][k]
    ans = max(ans,now)
print(ans)
            
    