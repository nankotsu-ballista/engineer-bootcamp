n=int(input())
s=set()
points=[]
for i in range(n):
  x,y=map(int,input().split())
  s.add((x,y))
  points.append((x,y))
count=0
for i in range(n):
    for k in range(i+1,n):
        #print(i,k)
        ay,ax=points[i]
        by,bx=points[k]
        if ay!=by and bx!=ax:
            if (ay,bx) in s and (by,ax) in s:
                count+=1
                #print(i,k,"atari")
print(count//2)
            
  