from collections import deque
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
count=[[0]*w for _ in range(h)]
q=deque()
checklist=[]
visited=[[False]*w for _ in range(h)]
for i in range(h):
    for k in range(w):
        if grid[i][k]=="#":
            visited[i][k]=True
            count[i][k]=1
            if i+1<h and visited[i+1][k]==False:
                count[i+1][k]+=1
                checklist.append((i+1,k))
            if i-1>-1 and visited[i-1][k]==False:
                count[i-1][k]+=1
                checklist.append((i-1,k))
            if k+1<w and visited[i][k+1]==False:
                count[i][k+1]+=1
                checklist.append((i,k+1))
            if k-1>-1 and visited[i][k-1]==False:
                count[i][k-1]+=1
                checklist.append((i,k-1))
#print(checklist)
# for i in count:
#     print(i)
while checklist:
    #print("checklist",checklist)
    # for i in count:
    #     print(i)
    for i,k in checklist:
        if count[i][k]==1:
            visited[i][k]=True
            q.append((i,k))
        elif count[i][k]>1:
            visited[i][k]=True
    checklist=[]
    #print(q)
    while q:
        i,k=q.popleft()
        if 1==1:
            visited[i][k]=True
            if i+1<h and visited[i+1][k]==False:
                count[i+1][k]+=1
                checklist.append((i+1,k))
            if i-1>-1 and visited[i-1][k]==False:
                count[i-1][k]+=1
                checklist.append((i-1,k))
            if k+1<w and visited[i][k+1]==False:
                count[i][k+1]+=1
                checklist.append((i,k+1))
            if k-1>-1 and visited[i][k-1]==False:
                count[i][k-1]+=1
                checklist.append((i,k-1))
ans=0
for i in range(h):
    for k in range(w):
        if count[i][k]==1:
            ans+=1
print(ans)
                
                
                
                
                
                
                
                
                
                
                
                
                