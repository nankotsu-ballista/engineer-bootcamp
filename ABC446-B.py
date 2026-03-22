n,m=map(int,input().split())
s=set()
for i in range(1,m+1):
    s.add(i)
for i in range(n):
    L=int(input())
    X=list(map(int,input().split()))
    check=False
    for i in X:
        check=False
        if i in s:
            print(i)
            s.discard(i)
            check=True
            break
    if check==False:
        print(0)
    
