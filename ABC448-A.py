n,x=map(int,input().split())
A=list(map(int,input().split()))
for i in range(n):
    if A[i]<x:
        x=A[i]
        print(1)
    else:
        print(0)