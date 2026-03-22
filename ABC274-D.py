n,x,y=map(int,input().split())
A=list(map(int,input().split()))
tates=set()
yokos=set()
yokos.add(A[0])
tates.add(0)
for i in range(1,n):
    tmp=set()
    if i%2==0:
        tmp=list(yokos)
        yokos=set()
        for k in tmp:
            yokos.add(k+A[i])
            yokos.add(k-A[i])
    if i%2==1:
        tmp=list(tates)
        tates=set()
        for k in tmp:
            tates.add(k+A[i])
            tates.add(k-A[i])
    # print("tate",tates)
    # print("yoko",yokos)
if x in yokos and y in tates:
    print("Yes")
else:
    print("No")
        