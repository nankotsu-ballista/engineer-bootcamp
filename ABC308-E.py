n=int(input())
A=list(map(int,input().split()))
S=input()
S=list(S)
M=[0]*3
ME=[[0]*3 for _ in range(3)]
ans=0
for i in range(n):
    if S[i]=="M":
        M[A[i]]+=1
    elif S[i]=="E":
        ME[0][A[i]]+=M[0]
        ME[1][A[i]]+=M[1]
        ME[2][A[i]]+=M[2]
    elif S[i]=="X":
        for j in range(3):
            for k in range(3):
                c=set()
                c.add(0)
                c.add(1)
                c.add(2)
                c.discard(j)
                c.discard(k)
                c.discard(A[i])
                c=list(c)
                if c:
                    ds=min(c)
                else:
                    ds=3
                ans+=ME[j][k]*ds
        
# print(M)
# for k in ME:
#     print(k)
print(ans)