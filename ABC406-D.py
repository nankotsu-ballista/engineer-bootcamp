h,w,n=map(int,input().split())
tate=[[] for _ in range(h+1)]
yoko=[[] for _ in range(w+1)]
tcheck=[True]*(h+1)
ycheck=[True]*(w+1)
used=[True]*(n)
for i in range(n):
    x,y=map(int,input().split())
    tate[x].append(i)
    yoko[y].append(i)
q=int(input())
#print(tate)
#print(yoko)
for i in range(q):
    ans=0
    vh,point=map(int,input().split())
    if vh == 1:
        if tcheck[point]==False:
            print(0)
        else:
            tcheck[point]=False
            for _ in range(len(tate[point])):
                s=tate[point].pop()
                if used[s] == True:
                    used[s] =False
                    ans+=1
            print(ans)
    elif vh == 2:
        if ycheck[point]==False:
            print(0)
        else:
            ycheck[point]=False
            for _ in range(len(yoko[point])):
                s=yoko[point].pop()
                if used[s] == True:
                    used[s] =False
                    ans+=1
            print(ans)
#print(ycheck)
    
    