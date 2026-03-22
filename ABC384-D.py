n,s=map(int,input().split())
a=list(map(int,input().split()))
s %= sum(a)
a=a+a
pre_sum=set()
p=0
pre_sum.add(p)
for d in a:
    p += d
    pre_sum.add(p)
for p in pre_sum:
    if (p + s) in pre_sum:
        print("Yes")
        exit()
print("No")
