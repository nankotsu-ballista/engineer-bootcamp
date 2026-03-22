x=int(input())
n=int(input())
w=list(map(int,input().split()))
q=int(input())
s=set()
sum=x
for i in range(q):
    p=int(input())
    if p not in s:
        s.add(p)
        sum+=w[p-1]
    else:
        s.discard(p)
        sum-=w[p-1]
    print(sum)

