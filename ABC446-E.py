m,a,b=map(int,input().split())
nodes=[[-1]*(m) for _ in range(m)]

# for i in range(m):
#     for k in range(m):
#         if visited[i][k]!=-1:
#             continue
#         di=i
#         dk=k
#         while visited[di][dk]==-1:
hukumu=set()
for i in range(m):
    for k in range(m):
        if i==0 or k==0:
            hukumu.add((i,k))
            
visited=[[-1]*(m) for _ in range(m)]
for i in range(1,m):
    for k in range(1,m):
        check=True
        if visited[i][k]!=-1:
            continue
        di=i
        dk=k
        tmp=[]
        while visited[di][dk]==-1:
            tmp.append((di,dk))
            visited[di][dk]=1
            di,dk=dk,(b*di+a*dk)%m
            if (di,dk) in hukumu:
                check=False
                break
        if check==False:
            for c,p in tmp:
                nodes[c][p]=0
                visited[c][p]=2
        else:
            if visited[di][dk]==1:
                for c,p in tmp:
                    nodes[c][p]=1
                    visited[c][p]=2
            elif visited[di][dk]==2:
                if nodes[di][dk]==0:
                    for c,p in tmp:
                        nodes[c][p]=0
                        visited[c][p]=2
                elif nodes[di][dk]==1:
                    for c,p in tmp:
                        nodes[c][p]=1
                        visited[c][p]=2
# for i in nodes:
#     print(i)
ans=0
for i in range(1,m):
    for k in range(1,m):
        if nodes[i][k]==-1:
            continue
        else:
            ans+=nodes[i][k]
print(ans)
        