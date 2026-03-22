N=int(input())
S=list(map(int,input().strip()))
signs=[]
#print(S)
for i in range(10):
    count=0
    for k in range(len(S)):
        if S[k]==i:
            count+=1
    signs.append(count)
#print(signs)
c=0
ans=0
while c**2<10**N+15:
    tmpsign=[0]*10
    tmp=str(c**2)
    tmp=list(tmp)
    for k in range(len(tmp)):
        tmpsign[int(tmp[k])]+=1
    tmpsign[0]+=N-len(tmp)
    # print(tmp)
    # print(tmpsign)
    if tmpsign == signs:
        ans+=1
    c+=1
print(ans)
    
    
