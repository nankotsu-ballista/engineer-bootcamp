t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s=list(s)
    ans=10**6
    cost=0
    zeroans=0
    count=0
    for k in s:
        if k == "0":
            count+=1
            zeroans=max(count,zeroans)
            cost+=2
        else:
            count=0
            zeroans=max(count,zeroans)
            cost+=1
            oneans=0
        
    ans=min(ans,cost-2*zeroans)
    cost=0
    oneans=0
    count=0
    for k in s:    
        if k == "1":
            count+=1
            oneans=max(count,oneans)
            cost+=2
        else:
            count=0
            oneans=max(count,oneans)
            cost+=1
    ans=min(ans,cost-2*oneans)
    print(ans)
            