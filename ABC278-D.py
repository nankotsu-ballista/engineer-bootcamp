n=int(input())
a=list(map(int,input().split()))
a=[0]+a
q=int(input())
sums=[0]*(n+1)
switchtime=[0]*(n+1)
check=False
lastswitchtime=-1
for i in range(q):
    que=list(map(int,input().split()))
    if que[0] == 1:
        sum=0
        number=que[1]
        check=True
        lastswitchtime=i
    elif que[0] == 2:
        if switchtime[que[1]]<lastswitchtime:
            sums[que[1]]=que[2]
        else:
            sums[que[1]]+=que[2]
        switchtime[que[1]]=i
    elif que[0] == 3:
        if check==False:
            print(a[que[1]]+sums[que[1]])
        else:
            if switchtime[que[1]]<lastswitchtime:
                print(number)
            else:
                print(number+sums[que[1]])
            
            