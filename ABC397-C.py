n=int(input())
A=list(map(int,input().split()))
maxvalueR=0
maxvalueL=0
summer=0
maxL=0
L=[0]*n
R=[0]*n
Lkazu=set()
Rkazu=set()
for i in range(n):
    Lkazu.add(A[i])
    L[i]=len(Lkazu)
for i in range(n):
    Rkazu.add(A[n-1-i])
    R[n-i-1]=len(Rkazu)
# print(L)
# print(R)
LL=0
for i in range(n-1):
    LL=max(L[i]+R[i+1],LL)
print(LL)