n, t = map(int, input().split())
tate=[0]*n
yoko=[0]*n
A=list(map(int,input().split()))
rcount=0
lcount=0
for i in range(t):
    v=(A[i]-1)//n
    h=(A[i]-1)%n
    # print(str(v)+" "+str(h))
    tate[v]+=1
    yoko[h]+=1
    # print(yoko)
    # print(tate)
    if v==h:
        rcount+=1
    if v+h==n-1:
        lcount+=1
    if tate[v]==n  or yoko[h]==n or rcount == n or lcount == n:
        print(i+1)
        exit()
    
print(-1)