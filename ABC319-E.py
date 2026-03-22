n,x,y=map(int,input().split())
busstops=[]
for i in range(n-1):
    p,t=map(int,input().split())
    busstops.append((p,t))
Q=int(input())
mods=[]
for i in range(840):
    mod=[]
    for k in range(8):
        mod.append(i%(k+1))
    mods.append(mod)
#print(mods)
sums=[]
for i in range(840):
    sum=i+x
    for k in range(n-1):
        #print(sum)
        p,t=busstops[k]
        if sum%p !=0:
            sum+=(p-(sum%p))
        sum+=t
    #print(sum)
    sum+=y
    sums.append(sum-i)
for i in range(Q):
    q=int(input())
    print(q+sums[q%840])