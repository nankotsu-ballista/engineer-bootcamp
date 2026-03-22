import sys
sys.setrecursionlimit(2 * 10 ** 5 + 10)
N,M=map(int,input().split())
if M==0:
    print("No")
    exit()
count=[0]*N
node = [[] for _ in range(N + 1)]
for i in range(M):
    A,B=map(int,input().split())
    count[A-1]+=1
    count[B-1]+=1
    node[A].append(B)
    node[B].append(A)
check1=True
for i in range(N):
    if count[i]!=2:
        check1=False
visited = [False] * (N + 1)
visited[0]=True
def dfs(i):
    if visited[i]== True:
        return
    visited[i]=True
    for nxt in node[i]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)
check2=True
for i in range(N+1):
    if visited[i]== True:
        continue
    else:
        check2=False
check3=False
if N==M:
    check3=True
if check1 and check2 and check3:
    print("Yes")
else:
    print("No")
    