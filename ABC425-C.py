n,q=map(int,input().split())
A=list(map(int,input().split()))
A=A
ruisekiwa=[0]
sum=0
for i in range(n):
    sum+=A[i]
    ruisekiwa.append(sum)
#print(ruisekiwa)
settei=0
for i in range(q):
    t=list(map(int,input().split()))
    if t[0]==1:
        settei+=t[1]
    elif t[0]==2:
        l=(t[1]+settei)%(n)
        r=(t[2]+settei)%(n)
        if r == 0:
            r=n
        if l == 0:
            l=n
        #print(l,r)
        if l<=r:
            print(ruisekiwa[r]-ruisekiwa[l-1])
        else:
            print(ruisekiwa[n]-ruisekiwa[l-1]+ruisekiwa[r]-ruisekiwa[0])

        