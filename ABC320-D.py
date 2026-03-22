from collections import deque
n,m=map(int,input().split())
pos=[[]for _ in range(n+1)]
poscheck=[False for _ in range(n+1)]
position=[[]for _ in range(n+1)]
#print(pos)
for i in range(m):
    A,B,X,Y=map(int,input().split())
    pos[A].append((B,X,Y))
    pos[B].append((A,-X,-Y))
q=deque()
q.append(1)
position[1]=(0,0)
poscheck[1]=True
while q:
    A=q.popleft()
    for B,X,Y in pos[A]:
        if poscheck[B]==False:
            x,y=position[A]
            position[B]=((x+X,y+Y))
            poscheck[B]=True
            q.append(B)
                

# print(poscheck)
# print(position)
for t in position[1:]:
    if t:
        print(t[0], t[1])
    else:
        print("undecidable")
    
            
            
        
        