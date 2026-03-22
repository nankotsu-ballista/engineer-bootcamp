T=int(input())
for _ in range(T):
    checkset=set()
    ans=0
    N=int(input())
    A=list(map(int,input().split()))
    t=[[]for _ in range(N+1)]
    #print(t)
    for i in range(2*N):
        t[A[i]].append(i)
    #print(t)
    check=[False for _ in range(N+1)]
    #print(check)
    for i in range(2*N-1):
        if A[i] == A[i+1]:
            check[A[i]]=True
    #print(check)
    for i in range(2*N-1):
        if check[A[i]] == True or check[A[i+1]] == True or (min(A[i],A[i+1]),max(A[i],A[i+1])) in checkset:
            continue
        else:
            ta1,ta2=t[A[i]]
            tb1,tb2=t[A[i+1]]
        ts=[ta1,ta2,tb1,tb2]
        ts.sort()
        #print(ts)
        if ts[1]-ts[0]==1 and ts[3]-ts[2]==1:
            ans+=1
            checkset.add((min(A[i],A[i+1]),max(A[i],A[i+1])))
    print(ans)