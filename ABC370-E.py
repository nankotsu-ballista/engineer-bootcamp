from collections import defaultdict
n,k=map(int,input().split())
A=list(map(int,input().split()))
ruiseki=[0]
tmp=0
mod=998244353
ruisekicounter=defaultdict(int)
for i in range(n):
    tmp+=A[i]
    ruiseki.append(tmp)
ruisekicounter[0]=1
anssums=[1]
anssum=1#今までの合計
ruisekicounter[0]=1
for i in range(1,n+1):
    need=ruiseki[i]-k
    dp=(anssum-ruisekicounter[need])%mod
    ruisekicounter[ruiseki[i]]=(ruisekicounter[ruiseki[i]]+dp)%mod
    anssum=(anssum+dp)%mod
    anssums.append(anssum)
    
# print(ruiseki)
# print(ruisekicounter)
# print(anssums)
print(dp%mod)