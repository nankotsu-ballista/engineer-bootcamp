n=int(input())
A=list(map(int,input().split()))
minhito=10**10
t=0
for i in range(n):
    t+=A[i]
    minhito=min(minhito,t)
#print(minhito)

if minhito<0:
    t=(-1)*minhito

    for i in range(n):
        t+=A[i]
    print(t)
else:
    print(t)