n,q=map(int,input().split())
x=list(map(int,input().split()))
sums=[0]
deiri=[[]for _ in range(n+1)]
sum=0
SUM=0
s=set()
for i in range(q):
    if x[i]in s:
        s.discard(x[i])
        sum-=1
        deiri[x[i]].append(i)
    else:
        s.add(x[i])
        sum+=1
        deiri[x[i]].append(i)
    SUM+=sum
    sums.append(SUM)
#print(deiri)
for i in range(n+1):
    if len(deiri[i])%2==1:
        deiri[i].append(q)
# print(deiri)
# print(sums)
answers=[0]*(n+1)
for i in range(n+1):
    sum=0
    if len(deiri[i])>1:
        for d in range(len(deiri[i])//2):
            sum+=sums[deiri[i][2*d+1]]-sums[deiri[i][2*d]]
        answers[i]=sum
print(*answers[1:])

            
             