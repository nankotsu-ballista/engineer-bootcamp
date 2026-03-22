N,M,Q=map(int,input().split())
alll=set()
kengen=[set() for _ in range(N+1)]
for i in range(Q):
    A=list(map(int,input().split()))
    if A[0]==1:
        kengen[A[1]].add(A[2])
    elif A[0]==2:
        alll.add(A[1])
    elif A[0]==3:
        if int(A[2]) in kengen[A[1]] or A[1] in alll:
            print("Yes")
        else:
            print("No")