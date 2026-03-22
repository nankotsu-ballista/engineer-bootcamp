n,x=map(int,input().split())
remains=set()
remains.add(x)
for i in range(n):
    a,b=map(int,input().split())
    c=list(remains)
    for k in c:
        for j in range(b+1):
            if k-(a*j)<0:
                break
            if k-(a*j) not in remains:
                remains.add(k-(a*j))
if 0 in remains:
    print("Yes")
else:
    print("No")
                