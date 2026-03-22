n=int(input())
S=list(input())
onecount=0
zerocount=0
ans=0
for i in range(n):
    tmponecount=0
    tmpzerocount=0
    if S[i]=="0":
        tmponecount=zerocount+onecount
        ans+=(zerocount+onecount)
        tmpzerocount=1
    if S[i]=="1":
        ans+=1
        ans+=zerocount
        tmponecount=zerocount
        tmpzerocount=onecount
        tmponecount+=1
    onecount=tmponecount
    zerocount=tmpzerocount
    #print(zerocount,onecount)
print(ans)