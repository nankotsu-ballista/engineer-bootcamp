from collections import deque
qq=int(input())
length=1
numbers=deque()
numbers.append(1)
ans=1
amari=[]
amasum=1
for i in range(6*10**5+1):
    amari.append(amasum)
    amasum=amasum*10
    amasum=amasum%998244353
#print(amari[:20])
for i in range(qq):
    #print(numbers)
    q=list(map(int,input().split()))
    if q[0]==1:
        x=q[1]
        numbers.append(x)
        ans=(ans*10+x)%998244353
        length+=1
    elif q[0]==2:
        x=numbers.popleft()
        ans-=(x*amari[length-1])%998244353
        ans=ans%998244353
        length-=1
    elif q[0]==3:
        print(ans)