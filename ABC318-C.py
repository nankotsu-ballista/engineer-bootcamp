N,D,P=map(int,(input().split()))
#print(N)
#print(M)
#graph = [[0] * (N + 1) for _ in range(N + 1)]
F = list(map(int, input().split()))
F.sort()
Q=len(F)//D
S=len(F)%D
#print(Q)
ans=0
for i in range(Q):
    sum=0
    for j in range(D):
        sum += F[D*i+j+S]
    if sum >= P:
        ans += P
    else:
        ans += sum


sum=0
for j in range(S):
    sum += F[j]
if sum >= P:
    ans += P
else:
    ans += sum

print(ans)
