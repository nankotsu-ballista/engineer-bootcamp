import bisect
n=int(input())
A=list(map(int,input().split()))
q=int(input())
A.sort()
if n==1:
    for i in range(q):
        b=int(input())
        print(abs(b-A[0]))
    exit()
for i in range(q):
    b=int(input())
    idx=bisect.bisect_left(A,b)
    if idx==0:
        print(min(abs(b-A[0]),abs(b-A[1])))
    elif idx==n or idx == (n-1):
        print(min(abs(b-A[n-1]),abs(b-A[n-2])))
    else:
        print(min(abs(b-A[idx]),abs(b-A[idx-1])))
    
    