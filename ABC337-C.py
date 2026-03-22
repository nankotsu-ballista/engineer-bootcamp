n=int(input())
A=list(map(int,input().split()))
count=[0]*(n+1)
for i in range(n):
    if A[i] == -1:
        continue
    count[A[i]]+=1
count[0]=1
lastidx=0
for i in range(n+1):
    if count[i]==0:
        lastidx=i
narabi=[]
nxtidx=lastidx
for i in range(n):
    narabi.append(nxtidx)
    nxtidx=A[nxtidx-1]
# print(count)
# print(lastidx)
# print(narabi)
narabi.reverse()
print(" ".join(map(str, narabi)))