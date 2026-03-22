N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
ans = T[:]

for _ in range(2):
  for i in range(N):
    next = (i + 1)%N
    ans[next] = min(ans[next],ans[i] + S[i])
    
for t in ans:
  print(t)