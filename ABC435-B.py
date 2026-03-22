n=int(input())
A=list(map(int,input().split()))
goukei=sum(A)
#print(A)
se=set()
ruiseki=[0]
tmp=0
for i in range(n):
    tmp+=A[i]
    ruiseki.append(tmp)
#print(ruiseki)
ans=0
for i in range(n):
    for k in range(i,n):
        tmp=0
        #print(i,k)
        #print(ruiseki[k+1]-ruiseki[i])
        check=True
        for c in range(i,k+1):
            if (ruiseki[k+1]-ruiseki[i])%A[c]==0:
                check=False
        if check==True:
            ans+=1
            #print(i,k)
print(ans)
            
            
        
    