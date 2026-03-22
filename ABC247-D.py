from collections import deque
q=int(input())
hiitasum=0
que=deque()
for i in range(q):
    Q=list(map(int,input().split()))
    num=Q[0]
    #print(que)
    if num==1:
        x,c=Q[1],Q[2]
        que.append((x,c))
    elif num ==2:
        c=Q[1]
        sum=0
        ans=0
        while True:
            number,count=que.popleft()
            ans+=count*number
            c-=count
            #print("s")
            if c<=0:
                que.appendleft((number,-c))
                ans-=abs(c*number)
                print(ans)
                break
            
        