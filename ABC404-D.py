n,m=map(int,input().split())
c=list(map(int,input().split()))
park=[[] for _ in range(n+1)]

for i in range(m):
    t=list(map(int,input().split()))
    t=t[1:]
    for j in t:
        park[j].append(i+1)
#print(park)#parkでみれる動物の一覧
ans=10**18
for i in range(3**n):
    t=[]
    go=True
    for j in range(n):
        t.append(i%3)
        i=i//3
    #print(t)
    check=[0]*m
    cost=0
    for g in range(n):
        if t[g]==1:
            for l in park[g+1]:
                check[l-1]+=1
            cost+=c[g]
        elif t[g] ==2:
            for l in park[g+1]:
                check[l-1]+=2
            cost+=c[g]*2
    for q in check:
        if q<2:
            go=False
    # print(check)
    # print(cost)
    if go ==True:   
        ans=min(ans,cost)
print(ans)