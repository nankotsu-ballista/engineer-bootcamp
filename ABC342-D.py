N=int(input())
A=list(map(int,input().split()))
t=[0]*(3*10**5)
zero=0
for k in range(N):
    s=A[k]
    if s ==0:
        zero+=1
        continue
    age=1
    for i in range(2,1000):
        count=0
        while s%i == 0:
            s=s//i
            count+=1
        if count%2==1:
            age=age*i
    if s > 1:
        age *= s
    t[age]+=1
ans=0

for i in range(3*10**5):
    if t[i]>1:
        ans+=(t[i]*(t[i]-1))//2
if zero!=0:
        ans+=zero*(zero-1)//2
        ans+=zero*(N-zero)
print(ans)
#print(t)
    