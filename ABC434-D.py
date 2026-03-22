n=int(input())
items=[]
width=2010
ruisekigrid=[[0]*width for _ in range(width)]
for i in range(n):
    u,d,l,r=map(int,input().split())
    items.append((u,d,l,r))
    ruisekigrid[u][l]+=1
    ruisekigrid[u][r+1]-=1
    ruisekigrid[d+1][r+1]+=1
    ruisekigrid[d+1][l]-=1
# for i in ruisekigrid:
#     print(i)
for i in range(width):
    sum=0
    for k in range(width):
        sum+=ruisekigrid[i][k]
        ruisekigrid[i][k]=sum
for k in range(width):
    sum=0
    for i in range(width):
        sum+=ruisekigrid[i][k]
        ruisekigrid[i][k]=sum
# for i in ruisekigrid:
#     print(i)
# print("")
kumocount=0
for i in range(1,2001):
    for k in range(1,2001):
        if ruisekigrid[i][k]!=0:
            kumocount+=1
for i in range(width):
    for k in range(width):
        if ruisekigrid[i][k]!=1:
            ruisekigrid[i][k]=0
# for i in ruisekigrid:
#     print(i)
# print("")
for i in range(width):
    sum=0
    for k in range(width):
        sum+=ruisekigrid[i][k]
        ruisekigrid[i][k]=sum
for k in range(width):
    sum=0
    for i in range(width):
        sum+=ruisekigrid[i][k]
        ruisekigrid[i][k]=sum

# for i in ruisekigrid:
#     print(i)
#print(kumocount)
for u,d,l,r in items:
    print(2000*2000-kumocount+ruisekigrid[d][r]-ruisekigrid[d][l-1]-ruisekigrid[u-1][r]+ruisekigrid[u-1][l-1])
    
    
    
            
    