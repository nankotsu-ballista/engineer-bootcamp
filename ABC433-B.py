n=int(input())
A=list(map(int,input().split()))
print(-1)
for i in range(1,n):
    tmp=-1
    for k in range(i-1,-1,-1):
        if A[k]>A[i]:
            tmp=k+1
            break
    print(tmp)