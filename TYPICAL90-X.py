import math
n,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
diff=0
for i in range(n):
    diff+=abs(A[i]-B[i])
if diff>k:
    print("No")
else:
    if diff%2 == k%2:
        print("Yes")
    else:
        print("No")
        