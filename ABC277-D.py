from collections import defaultdict
n,m=map(int,input().split())
A=list(map(int,input().split()))
cards=defaultdict(int)
s=set()
for i in A:
    cards[i]+=1
    s.add(i)
s=list(s)
them=[]
#print(cards)
for i in s:
    them.append((i,cards[i]))
#print(them)
length=len(them)
them.sort()
them=them+them

#print(them)
ans=0
i=0
while i<=length-1:
    sum=them[i][0]*them[i][1]
    beforeidx=them[i][0]
    ans=max(ans,sum)
    check=False
    for k in range(i+1,i+length):
        #print(i,k)
        if (beforeidx+1)%m!=them[k][0]:
            ans=max(ans,sum)
            i=k
            check=True
            break
        else:
            beforeidx=them[k][0]
            sum+=them[k][0]*them[k][1]
        ans=max(ans,sum)
    if check==False:
        break
    
    

rui=0
for i in A:
    rui+=i
print(rui-ans)
#print()
        