N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(N):
    for j in range(M):
        if A[i]==B[j] and A[i]!=-1:
            A[i]=-1
            B[j]=-1
#print(A)
#print(B)
ans=[]
for i in range(N):
    if A[i]!= -1:
        ans.append(A[i])
ans=[str(a) for a in ans]
ans=" ".join(ans)
print(ans)