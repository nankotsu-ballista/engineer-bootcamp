import bisect
N,Q=map(int,(input().split()))
R=list(map(int,(input().split())))
R.sort()
summer=[0]*N
sum=0
for i in range(N):
    sum+=R[i]
    summer[i]=sum
    
for i in range(Q):
    X = int(input())
    idx = bisect.bisect_right(summer,X)
    print(idx)