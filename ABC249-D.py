n=int(input())
A=list(map(int,input().split()))
s=set()
for i in range(1,2*10**5+1):
    for k in range(1,2*10**5 // i + 1):
        j=i*k
        if j>2*10**5:
            break
        s.add((i,j,k))
count=[0]*(2*10**5+1)
for i in range(n):
  count[A[i]]+=1
ans=0
for i in s:
  p,q,r=i
  ans+=count[p]*count[q]*count[r]
print(ans)