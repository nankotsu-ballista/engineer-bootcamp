n,x,y=map(int,input().split())
ans=0
A2=list(map(int,input().split()))
Alist=[]
start=-1
for i in range(n):
    if A2[i]>x or A2[i]<y:
        if start!=-1:
            Alist.append((start,i-1))
            start=-1
    else:
        if start==-1:
            start=i
if start!=-1:
    Alist.append((start,i))
#print(Alist)
    
for al,af in Alist:
    n=af-al+1
    A=A2[al:af+1]
    #print(A)
    mincheck=False
    maxcheck=False
    xsum=0
    ysum=0
    xysum=0
    start=-1
    canmake=[]
    allsum=n*(n+1)//2
    for i in range(n):
        if A[i]==x:
            if start!=-1:
                canmake.append((start,i-1))
                start=-1
        else:
            if start==-1:
                start=i
    if start!=-1:
        canmake.append((start,i))
    #print(canmake)
    for i,k in canmake:
        nd=k-i+1
        xsum+=nd*(nd+1)//2
    
    
    start=-1
    canmake=[]
    for i in range(n):
        if A[i]==y:
            if start!=-1:
                canmake.append((start,i-1))
                start=-1
        else:
            if start==-1:
                start=i
    if start!=-1:
        canmake.append((start,i))
    #print(canmake)
    for i,k in canmake:
        nd=k-i+1
        ysum+=nd*(nd+1)//2
    
    start=-1
    canmake=[]
    for i in range(n):
        if A[i]==y or A[i]==x:
            if start!=-1:
                canmake.append((start,i-1))
                start=-1
        else:
            if start==-1:
                start=i
    if start!=-1:
        canmake.append((start,i))
    #print(canmake)
    for i,k in canmake:
        nd=k-i+1
        xysum+=nd*(nd+1)//2
    # print(xsum)
    # print(ysum)
    # print(xysum)
    # print(allsum)
    #print(allsum-xsum-ysum+xysum)
    tmpans=(allsum-xsum-ysum+xysum)
    ans+=tmpans
print(ans)







