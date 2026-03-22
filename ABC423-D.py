import heapq
n,k=map(int,(input().split()))
time=0
inshop=0
eating=[]
heapq.heapify(eating)
intime=[]
for i in range(n):
    waitstarttime,staytime,ninzuu=map(int,(input().split()))
    #いけるなら入れる
#
    if inshop <= k - ninzuu:
        # print(inshop)
        # print(k - ninzuu)
        time=max(waitstarttime,time)
        heapq.heappush(eating,(time+staytime,ninzuu))
        inshop += ninzuu
        intime.append(time)
    else:
        #無理ならぬく
        while inshop > k - ninzuu:
            tt,kazu=(heapq.heappop(eating))
            inshop-=kazu
            time=tt
        time=max(waitstarttime,time)
        heapq.heappush(eating,(time+staytime,ninzuu))
        inshop += ninzuu
        intime.append(time)
for i in intime:
    print(i)
            
            