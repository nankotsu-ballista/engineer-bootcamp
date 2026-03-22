n,m=map(int,input().split())
point=[0]*n
votes=[input() for _ in range(n)]
minner=[0]*m
for j in range(m):
    zero=0
    one=0
    for i in range(n):
        if votes[i][j]=="1":
            one+=1
        else:
            zero+=1
    if one<zero:
        minner[j]=1
    else:
        minner[j]=0
#print(minner)
for j in range(m):
    if minner[j]==1:
        for i in range(n):
            if votes[i][j]=="1":
                point[i]+=1
    else:
        for i in range(n):
            if votes[i][j]=="0":
                point[i]+=1
#print(max(point))
ans=[]
for i in range(n):
    if point[i]==max(point):
        ans.append(str(i+1))
result = ' '.join(ans)
print(result)
        
        