import heapq

q=int(input())
hq=[]
gene=0
ruiseki=0
genes=[0]*(2*10**5+1)
for i in range(q):
    #print(hq,gene)
    que=list(map(int,input().split()))
    if que[0]==1:
        heapq.heappush(hq,(que[1]-ruiseki,gene,ruiseki))
    elif que[0]==2:
        gene+=1
        ruiseki+=que[1]
        genes[gene]=ruiseki
    elif que[0]==3:
        num,gen,ru=heapq.heappop(hq)
        print(num+genes[gene]-genes[gen]+ru)
#print(genes)
            
            