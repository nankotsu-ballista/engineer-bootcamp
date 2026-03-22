from collections import deque
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
#A=deque(A)
# sun=0
# sunner=[0]*N
# for i in range(N):
#     sun+=A[i]
#     sunner[i]=sun
#print(sunner)
# for i in range(K):
#     if A[1]-A[0]>A[-1]-A[-2]:
#         A.popleft()
#     else:
#         A.pop()
#     #print(A)
#print(A)
mostmin=10**18
for i in range(K+1):
    mini=A[i+(N-K)-1]-A[i]
    mostmin=min(mini,mostmin)
print(mostmin)
