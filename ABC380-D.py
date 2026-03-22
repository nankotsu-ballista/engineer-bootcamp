s=input()
q=int(input())
K=list(map(int,input().split()))
l=len(s)
pqq=[]
for i in range(q):
    count=0
    tt=(s[K[i]%l-1])
    for k in list(bin((K[i]-1)//l)):
        if k=="1":
            count+=1
    #print(bin(K[i]//l))
    if count%2==1:
        pqq.append(tt.swapcase())
    else:
        pqq.append(tt)
print(*pqq)
