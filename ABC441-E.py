n=int(input())
S=list(input())
diff=[0]*(10**6+1000)
Asum=0
Bsum=0
As=[]
Bs=[]
AminBs=[0]
for i in range(n):
    if S[i]=="A":
        Asum+=1
    if S[i]=="B":
        Bsum+=1
    As.append(Asum)
    Bs.append(Bsum)
# print(As)
# print(Bs)
for i in range(n):
    AminBs.append(As[i]-Bs[i])
diffsum=0
ans=0
diff[0]=1
for i in range(1,n+1):
    if AminBs[i]>AminBs[i-1]:
        diffsum+=diff[AminBs[i-1]]
    elif AminBs[i]<AminBs[i-1]:
        diffsum-=diff[AminBs[i]]
    diff[AminBs[i]]+=1

    ans+=diffsum
print(ans)
    