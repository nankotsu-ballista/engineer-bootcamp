n=int(input())
a=list(map(int,input().split()))
a.sort()
r=n
cnt = 0
res = 0
for i in range(n):
    r = max(r,i + 1)
    while r - 1 > i and a[r - 1] + a[i] >= 100000000:
        r -=1
    cnt += n-r
for i in range(n):
    res +=a[i]* (n-1)
    
res -= cnt * 100000000
#print(cnt)
print(res)