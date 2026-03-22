N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
umami=[-1]*(2*10**5+1)
r=2*10**5
for i in range(N):
    if A[i]<=r:
        umami[A[i]:r+1]=[i+1]*(r-A[i]+1)
        r=A[i]-1
for b in B:
    print(umami[b])