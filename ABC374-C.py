from collections import defaultdict
n=int(input())
K=list(map(int,input().split()))
summer=0
for i in range(n):
    summer+=K[i]
ans=10**20
for bit in range(1 << n):
    temposum=0
    for i in range(n):
        if bit & (1 << i):
            temposum+=K[i]
    tempoanother=summer-temposum
    tempoans=max(tempoanother,temposum)
    ans=min(tempoans,ans)
            
print(ans)