N, M=map(int,(input().split()))
B=list(map(int,(input().split())))
W=list(map(int,(input().split())))
B.sort(reverse=True)
W.sort(reverse=True)
Bruiseki=[0]*(N+1)
Wruiseki=[0]*(M+1)
maxW=[0]*(M+1)
for i in range(N):
    Bruiseki[i + 1] = Bruiseki[i] + B[i]
for i in range(M):
    Wruiseki[i + 1] = Wruiseki[i] + W[i]
    maxW[i + 1] = max(maxW[i], Wruiseki[i + 1])
ans = 0
for i in range(N + 1):
    ans = max(ans, Bruiseki[i] + maxW[min(i, M)])
print(ans)