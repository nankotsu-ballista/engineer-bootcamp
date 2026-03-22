from collections import defaultdict
n,m=map(int,input().split())
A=list(map(int,input().split()))
L=0
R=max(A)
if sum(A) <= m:
    print("infinite")
    exit()
while L<R:
    mid=(L+R+1)//2
    summer=0
    for i in range(n):
        summer+=min(A[i],mid)
    if summer>m:
        R=mid-1
    else:
        L=mid
print(L)