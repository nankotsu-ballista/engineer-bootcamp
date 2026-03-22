import heapq
n,k=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
s=set()
count=0
costs=[0]
cost=set()
while costs:
    #print(costs)
    tmp=heapq.heappop(costs)
    for i in A:
        if tmp+i not in cost:
            cost.add(tmp+i)
            count+=1
            heapq.heappush(costs,tmp+i)
            if count==2*10**6+1:
                cost=list(cost)
                cost.sort()
                print(cost[k-1])
                exit()
        