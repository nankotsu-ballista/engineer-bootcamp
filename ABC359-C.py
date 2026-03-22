sx,sy=map(int,input().split())
tx,ty=map(int,input().split())
hdiff=abs(ty-sy)
if (tx+ty)%2==1:
    tx=(tx,tx-1)
else:
    tx=(tx,tx+1)
if (sx+sy)%2==1:
    sx=(sx,sx-1)
else:
    sx=(sx,sx+1)
# print(sx)
# print(tx)
mindiff=10**18
for i in range(2):
    for j in range(2):
        mindiff=min(abs(sx[i]-tx[j]),mindiff)
if hdiff>=mindiff:
    print(hdiff)
else:
    print(hdiff+(mindiff-hdiff+1)//2)