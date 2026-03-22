n,m=map(int,input().split())
X=list(map(int,input().split()))
A=list(map(int,input().split()))
pairs = sorted(zip(X, A))
sum=0
cost=0
for x,a in pairs:
    if sum< x-1:
        print(-1)
        exit()
    sum+=a
    cost+=a*x
if sum!=n:
    print(-1)
    exit()
print(n*(1+n)//2-cost)
    
    
    