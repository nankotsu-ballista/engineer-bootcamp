n=int(input())
A=list(map(int,input().split()))
ans=1
tmp=A[0]
for i in range(1,n):
    if tmp>i:
        ans+=1
    else:
        print(ans)
        exit()
    if tmp<A[i]+i:
        tmp=A[i]+i
print(ans)
    
    