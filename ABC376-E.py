import heapq
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=[]
    for i in range(n):
        C.append((A[i],B[i]))
    C.sort()
    C.reverse()
    #print(C)
    hq=[]
    for i in range(1,n):
        heapq.heappush(hq,(C[i][1],i))
    #print(C)
    ans=10**18
    s=set()
    sum=0
    #print(hq)
    for i in range(k-1):
        number,idx=heapq.heappop(hq)
        s.add(idx)
        sum+=number
    #print("sum",sum)
    for i in range(n-k+1):
        if i in s:
            sum-=C[i][1]
            while True:
                #print(hq)
                number,idx=heapq.heappop(hq)
                if idx in s or idx <=i:
                    continue
                s.add(idx)
                sum+=number
                break
        #print("i回目",i)     
        #print(C[i][0]*(C[i][1]+sum))
        ans=min(ans,C[i][0]*(C[i][1]+sum))
    print(ans)
    
    