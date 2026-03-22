n,m=map(int,input().split())
A=list(map(int,input().split()))
hyousuu=[0]*(n+1)
maxidx=0
maxhyou=0
for i in range(m):
    hyousuu[A[i]]+=1
    if (maxhyou==hyousuu[A[i]] and maxidx>A[i]) or maxhyou<hyousuu[A[i]]:
        maxhyou=hyousuu[A[i]]
        maxidx=A[i]
    print(maxidx)