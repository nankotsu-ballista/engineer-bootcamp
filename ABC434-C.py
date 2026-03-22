tt= int(input())
for _ in range(tt):
    #print(tt)
    n,h=map(int,input().split())
    check=True
    nowtime=0
    beforehigh=h
    beforelow=h
    for _ in range(n):
        t,l,u=map(int,input().split())
        timediff=t-nowtime
        nowtime=t
        nexthigh=beforehigh+timediff
        nextlow=beforelow-timediff
        if nextlow>u or nexthigh<l:
            check=False
        beforelow=max(nextlow,l,1)
        beforehigh=min(nexthigh,u)
        #print(beforelow,beforehigh)
    if check==False:
        print("No")
    if check==True:
        print("Yes")