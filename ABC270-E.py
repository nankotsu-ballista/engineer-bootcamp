n,k=map(int,input().split())
A=list(map(int,input().split()))
B=A[:]
A.sort()
ruiseki=[]
others=[]
sum=0
#print(A)
for i in A:
    sum+=i
    ruiseki.append(sum)
#print(ruiseki)
for i in range(len(A)):
    egf=(n-i-1)*A[i]
    others.append(egf)
#print(others)
asikiri=10**18
for i in range(n):
    kei=ruiseki[i]+others[i]
    if kei>k:
        if i==0:
            asikiri=0
        else:
            asikiri=A[i-1]
        break
    
#print(asikiri)
#print(B)
#print(k)
cnt=0
for i in range(n):
    if B[i]<=asikiri:
        k-=B[i]
        B[i]=0
    else:
        k-=asikiri
        B[i]=B[i]-asikiri
        cnt+=1
#print(k)
#print(B)
if cnt==0:
    print(*B)
    exit()
shou=k//cnt

for i in range(n):
    if B[i]==0:
        continue
    B[i]=B[i]-shou
    k-=shou
#print(B)
#print(k)
if k==0:
    print(*B)
    exit()
for i in range(n):
    if k==0:
        break
    if B[i]==0:
        continue
    B[i]=B[i]-1
    k-=1
print(*B)

        
        