t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        a[i]=a[i]%m
        b[i]=b[i]%m
    a.sort(reverse=True)
    b.sort()
    # print(a)
    # print(b)
    count=0
    idx=0
    for t in a:
        while idx<n and b[idx]+t<m:
            idx+=1
        if idx == n:
            break
        count+=1
        idx+=1
    print(sum(a)+sum(b)-m*count)
        
    
    