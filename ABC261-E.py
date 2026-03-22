n,c=map(int,input().split())
allone=[]
allzero=[]
for i in range(30):
    allone.append(1)
    allzero.append(0)
C=(bin(c))
c=[]
for i in range(32-len(C)):
    c.append(0)
for i in range(len(C)-2):
    c.append(int(C[i+2]))
for i in range(n):
    t,a=map(int,input().split())
    A=(bin(a))
    a=[]
    for i in range(32-len(A)):
        a.append(0)
    for i in range(len(A)-2):
        a.append(int(A[i+2]))
    if t==1:
        for keta in range(30):
            if allone[keta]==1 and a[keta]==1:
                allone[keta]=1
            else:
                allone[keta]=0
            if allzero[keta]==1 and a[keta]==1:
                allzero[keta]=1
            else:
                allzero[keta]=0
    elif t==2:
        for keta in range(30):
            if allone[keta]==0 and a[keta]==0:
                allone[keta]=0
            else:
                allone[keta]=1
        for keta in range(30):
            if allzero[keta]==0 and a[keta]==0:
                allzero[keta]=0
            else:
                allzero[keta]=1
        
    elif t==3:
        for keta in range(30):
            if (allone[keta]==1 and a[keta]==0) or (allone[keta]==0 and a[keta]==1):
                allone[keta]=1
            else:
                allone[keta]=0
            if (allzero[keta]==1 and a[keta]==0) or (allzero[keta]==0 and a[keta]==1):
                allzero[keta]=1
            else:
                allzero[keta]=0
    for keta in range(30):
        if c[keta]==1:
            c[keta]=allone[keta]
        elif c[keta]==0:
            c[keta]=allzero[keta]
    ans=0
    for d in range(30):
        ans+=c[d]*2**(29-d)
    print(ans)
    
    