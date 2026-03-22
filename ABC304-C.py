from collections import deque
N, D = map(int, input().split())
human = []
for _ in range(N):
    x, y = map(int, input().split())
    human.append((x, y))   
virus=[0]*N
checkkansen=[0]*N
checkkansen[0]=True
q = deque()
q.append(0)
while q:
    i = q.popleft()
    for j in range(N):
        if checkkansen[j]:
            continue
        dx = human[i][0] - human[j][0]
        dy = human[i][1] - human[j][1]
        if dx * dx + dy * dy <= D * D:
            checkkansen[j] = True
            q.append(j)


 
for i in range(N):
    if checkkansen[i] == True:
        print("Yes")
    else:
        print("No")
        