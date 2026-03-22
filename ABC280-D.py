k=int(input())
i=2
tmp=k
yakusu=set()
while i!=2*10**6+1:
    while k%i == 0:
        k=k//i
        yakusu.add(i)
    i+=1
yakusu.add(k)
yakusu=list(yakusu)
yakusu.sort()
#print(yakusu)
if len(yakusu)==0:
    print(k)
    exit()
if max(yakusu)>=10**6:
    print(max(yakusu))
    exit()
ans=1
k=tmp
for i in range(1,2*10**6+1):
    ans=ans*i%k
    if ans==0:
        print(i)
        exit()
    
