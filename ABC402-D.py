from collections import defaultdict
cnt = defaultdict(int)
n,m=map(int,input().split())
for i in range(m):
    a,b=map(int,input().split())
    q=(a+b)%n+1
    cnt[q]+=1
sum=0
for v in cnt.values():
    sum+=(v*(v-1)//2)
print(m*(m-1)//2-sum)