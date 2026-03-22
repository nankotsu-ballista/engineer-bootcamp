import bisect
n,q=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ruisekiwa=[0]*n
#print(A)
goukei=0
for i in range(n):
    goukei+=A[i]
    ruisekiwa[i]=goukei
#print(ruisekiwa)
maxa=max(A)
for i in range(q):
    b=int(input())
    idx=bisect.bisect_left(A,b)
    if idx==0:
        print((b-1)*(n)+1)
        continue
    if maxa<b:
        print(-1)
        continue
    ans =ruisekiwa[idx-1]+(b-1)*(n-idx)+1
    #print((b-1)*(n-idx))
    print(ans)

        