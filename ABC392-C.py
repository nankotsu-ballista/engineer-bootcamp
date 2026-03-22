N=int(input())
P=[0]+list(map(int,input().split()))
Q=[0]+list(map(int,input().split()))

ans=[0]*(N+1)
for i in range(1,N+1):
  ans[Q[i]]=Q[P[i]]

print(*ans[1:])