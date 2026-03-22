N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
L=int(input())
C=list(map(int,input().split()))
Q=int(input())
X=list(map(int,input().split()))
grid=[[0]*(M) for _ in range(N)]
last=set()
for i in range(N):
    for j in range(M):
        last.add(A[i]+B[j])
check=False
#print(last)
kye=[]
for i in range(Q):
    check=False
    for j in range(L):
        kye.append(X[i]-C[j])
        if (X[i]-C[j]) in last:
            check=True
    if check:
        print("Yes")
    else:
        print("No")
#print(kye)