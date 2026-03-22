n,m=map(int,input().split())
A=list(map(int,input().split()))
summer=sum(A)
for i in range(n):
    if summer-A[i]==m:
        print("Yes")
        exit()
print("No")