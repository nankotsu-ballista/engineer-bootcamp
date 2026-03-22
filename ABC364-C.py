n,x,y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
syoppai=0
amai=0
syoppaidx=n
amaidx=n
A.sort(reverse=True)
B.sort(reverse=True)
for i in range(n):
    amai+=A[i]
    if amai>x:
        amaidx=i+1
        break
for j in range(n):
    #print(syoppai)
    syoppai+=B[j]
    if syoppai>y:
        syoppaidx=j+1
        break
ans=min(syoppaidx,amaidx)
# print(amaidx)
# print(syoppaidx)
print(ans)