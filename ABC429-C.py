n=int(input())
A=list(map(int,input().split()))
sumi=(n*(n-1)*(n-2))//6
count=[0]*(n+1)
s=set()
for i in range(n):
    count[A[i]]+=1
    s.add(A[i])
#print(count)
ans=0
for i in range(n+1):
    if count[i]<1:
        continue
    else:
        ans+=(count[i]*(count[i]-1)//2)*(n-count[i])
print(ans)
    
    
        