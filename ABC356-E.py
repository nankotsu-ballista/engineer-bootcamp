n=int(input())
A=list(map(int,input().split()))
A.sort()
Acount=[0]*(2000001)
for i in range(n):
    Acount[A[i]]+=1
#print(Acount)
tmp=0
Acountruiseki=[]
for i in Acount:
    tmp+=i
    Acountruiseki.append(tmp)
#print(Acountruiseki)
ans=0
for i in range(1,max(A)+1):
    if Acount[i]==0:
        continue
    for k in range(2,(1000000//i)+2):
        haninokazu=Acountruiseki[i*k-1]-Acountruiseki[i*(k-1)-1]
        ans+=Acount[i]*(k-1)*haninokazu
        # if i==2 and k<10:
        #     print(i*(k-1)-1,i*k-1,ans)
    ans-=((Acount[i]+1)*Acount[i])//2

#print(Acountruiseki[:15])
print(ans)