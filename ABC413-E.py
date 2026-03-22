t=int(input())
for _ in range(t):
    n=int(input())
    P=list(map(int,input().split()))
    #print(P[0:3])
    for i in range(n):
        leng=2**i
        for k in range(len(P)//(2**(i+1))):
            #print(leng*2*k,leng*2*k+leng)
            if P[leng*2*k]>P[leng*2*k+leng]:
                P[leng*2*k:leng*2*k+leng],P[leng*2*k+leng:leng*2*k+leng+leng]=P[leng*2*k+leng:leng*2*k+leng+leng],P[leng*2*k:leng*2*k+leng]
    print(*P)