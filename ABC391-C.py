n,q=map(int,input().split())
count=n
hato=[0]*(n+1)
for i in range(n+1):
    hato[i]=i
hatokazu=[1]*(n+1)
sunokazu=0
#print(hato)
for i in range(q):
    A=list(map(int,input().split()))
    if A[0]==1:
        hatokazu[hato[A[1]]]-=1
        if hatokazu[hato[A[1]]]==1:
            sunokazu-=1
        hatokazu[A[2]]+=1
        if hatokazu[A[2]]==2:
            sunokazu+=1
        hato[A[1]]=A[2]
    elif A[0]==2:
        print(sunokazu)
# print(hato)
# print(hatokazu)