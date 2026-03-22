n=int(input())
L=list(map(int,input().split()))
check=[False]*(n+1)
sum=0
for i in range(n):
    if L[i]==1:
        break
    else:
        check[i+1]=True
for i in range(n):
    if L[n-i-1]==1:
        break
    else:
        check[n-i-1]=True
check[0]=True
check[n]=True
#print(check)
ans=0
for i in check:
    if i == False:
        ans+=1
print(ans)