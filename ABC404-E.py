n=int(input())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
ans=0
for i in range(n-2,-1,-1):
    if a[i]!=0:
        ans+=1
        minrange=10**10
        minidx=-1
        check=False
        for k in range(1,c[i]+1):
            if i-k<0:
               a[i]=0
               check=True
               break
            if a[i-k]!=0:
                a[i-k]+=a[i]
                a[i]=0
                check=True
                break
            if i-k-c[i-k]<minrange:
                minrange=i-k-c[i-k]
                minidx=i-k
        #print(i,minidx,check)
        if check==False:
            a[minidx]+=a[i]
            a[i]=0
print(ans)
            
                
            