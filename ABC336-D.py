from collections import deque
N=int(input())
A=list(map(int,input().split()))
L=[0]*N
for i in range(N):
    if i == 0:
        L[i] = min(A[i], 1)
    else:
        L[i] = min(A[i], L[i-1] + 1)
R = [0]*N
for i in range(N-1, -1, -1):
    if i == N-1:
        R[i] = min(A[i], 1)
    else:
        R[i] = min(A[i], R[i+1] + 1)    
ans=0
for i in range(N):
    ans=max(ans,min(L[i],R[i]))
print(ans)