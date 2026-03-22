import heapq
n,m=map(int,input().split())
nodes=[[]for _ in range(n+1)]
stoptime=[[]for _ in range(n+1)]
L=[]
D=[]
K=[]
sihatu=[]
syuden=[]
hq=[]
finaltime=[-1]*(n+1)
for i in range(m):
    l,d,k,c,A,B=map(int,input().split())
    nodes[B].append((A,c,i))
    L.append(l)
    D.append(d)
    K.append(k)
    sihatu.append(l)
    syuden.append(l+d*(k-1))
    if B==n:
        if finaltime[A]<l+d*(k-1):
            heapq.heappush(hq,(-(l+d*(k-1)),A))
            finaltime[A]=l+d*(k-1)
while hq:
    #print(hq)
    time,point=heapq.heappop(hq)
    time=-time
    for nxtstation,c,ldkid in nodes[point]:
        l,d,k=L[ldkid],D[ldkid],K[ldkid]
        #print(l,d,k,ldkid)
        if l>time-c:
            continue
        if l+d*(k-1)<time-c:
            expecttime=l+d*(k-1)
        else:
            expecttime=l+(((time-c)-l)//d)*d
        #print(expecttime)
        if finaltime[nxtstation]<expecttime:
            finaltime[nxtstation]=expecttime
            heapq.heappush(hq,(-expecttime,nxtstation))
    
    
# print(sihatu)
# print(syuden)
#print(finaltime)
for i in range(1,n):
    if finaltime[i]==-1:
        print("Unreachable")
    else:
        print(finaltime[i])
