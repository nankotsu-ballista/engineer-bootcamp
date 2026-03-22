n,m=map(int,input().split())
#print(int(m**(1/2)))
s=set()
for i in range(1,10**6+1):
    if i>n:
        break
    firstidx=m//i
    if firstidx>n:
        continue
    else:
        if firstidx*i==m:
            s.add(firstidx*i)
        if firstidx*(i+1)>=m and (firstidx+1)<=n:
            s.add((firstidx+1)*i)
#print(s)
s=list(s)
s.sort()
for i in range(len(s)):
    if s[i]>=m:
        print(s[i])
        exit()
print(-1)