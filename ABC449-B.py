h,w,q=map(int,input().split())
ans=h*w
for _ in range(q):
    num,t=map(int,input().split())
    if num==1:
        h-=t
        print(t*w)
    elif num==2:
        w-=t
        print(h*t)