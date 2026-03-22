import heapq
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
x=int(input())
mochiset=set()
toutatu=set()
hq=[]
for i in B:
    mochiset.add(i)
heapq.heappush(hq,0)
#print(mochiset)
while hq:
    #print(hq)
    tmp = heapq.heappop(hq)
    if tmp == x:
        print("Yes")
        exit()
    if tmp > x:
        print("No")
        exit()
    for i in A:
        if tmp+i not in mochiset and tmp+i not in toutatu:
            toutatu.add(tmp+i)
            heapq.heappush(hq,tmp+i)
if x in toutatu:
    print("Yes")
else:
    print("No")
            
    

