from collections import deque
N,K= map(int,input().split())
#S = [list(input()) for _ in range(H)]
sum=0
for i in range(N+1):
    sum+=i*100*K
for i in range(K+1):
    sum+=i*N
print(sum)