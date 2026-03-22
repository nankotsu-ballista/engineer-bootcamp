q=int(input())
number=[0]*(10**6+1)
forcount=set()
for i in range(q):
    A = list(map(int, input().split()))
    if A[0]==1:
        forcount.add(A[1])
        number[A[1]]+=1
    elif A[0]==2:
        number[int(A[1])]-=1
        if number[int(A[1])]==0:
            forcount.remove(A[1])
    elif A[0]==3:
        print(len(forcount))