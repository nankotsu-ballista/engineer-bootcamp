x,y=map(int,input().split())
a=(x+y)%12
if a!=0:
    print(a)
else:
    print(12)