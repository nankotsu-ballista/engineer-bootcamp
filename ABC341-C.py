H,W,N=map(int,input().split())
T=input()
grid = [list(input()) for _ in range(H)]
def idou(y,x,S):
    x=x
    y=y
    for i in range(N):
        if  x<0 or x>=W or y<0 or y>=H:
            return False
        if grid[y][x] == "#":
            return False
        if S[i] =="L":
            x-=1
        elif S[i] =="R":
            x+=1
        elif S[i] =="U":
            y-=1
        elif S[i] =="D":
            y+=1
        if  x<0 or x>=W or y<0 or y>=H:
            return False
        if grid[y][x] == "#":
            return False
    return True     
count=0
for i in range(H):
    for j in range(W):
        if idou(i,j,T):
            count +=1
print(count)
#print(idou(1,1,T))
        