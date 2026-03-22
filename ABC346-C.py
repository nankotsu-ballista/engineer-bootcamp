n,k=map(int,input().split())
a=list(map(int,input().split()))
num=set()
numsum=((1+k)*k)//2
#print(numsum)
for i in range(n):
    if a[i]<=k:
        num.add(a[i])
num=list(num)
#print(num)
print(numsum-sum(num))