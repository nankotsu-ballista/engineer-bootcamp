import heapq
h,w,x=map(int,input().split())
p,q=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(h)]
#print(S)
slimes=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
heapq.heappush(slimes,(0,p-1,q-1))
strong=S[p-1][q-1]
visited=[[False]*w for _ in range(h)]
while slimes:
    slime,i,k= heapq.heappop(slimes)
    if visited[i][k]==True:
        continue
    visited[i][k]=True
    if slime*x<strong:
        strong+=slime
        #print(slime)
        for d in range(4):
            nx=dx[d]+i
            ny=dy[d]+k
            if 0<=nx<h and 0<=ny<w and visited[nx][ny]==False:
                heapq.heappush(slimes,(S[nx][ny],nx,ny))
    else:
        break
print(strong)
#print(202+106+336+212+487)
# for a in visited:
#     print(a)