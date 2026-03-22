q=int(input())
f=[]
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        f.append(a[1])
    else:
        print(min(f))
        f.remove(min(f))
        #print(f)