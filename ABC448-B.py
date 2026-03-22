n,m=map(int,input().split())
C=list(map(int,input().split()))
saisyo=sum(C)
use=0
for i in range(n):
    a,b=map(int,input().split())
    use+=b
    C[a-1]-=b
# print(use)
# print(C)
for i in C:
    if i<0:
        use+=i
print(use)
    
    