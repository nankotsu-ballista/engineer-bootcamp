n=int(input())
ss=[]
for i in range(n):
    s=input()
    ss.append((s,i))
ss.sort()
lists=[0]*n
#print(ss)
for i in range(n):
    if i==0 or i==n-1:
        continue
    S1=list(ss[i-1][0])
    S2=list(ss[i][0])
    S3=list(ss[i+1][0])
    befoans=0
    aftans=0
    for k in range(min(len(S1),len(S2))):
        if S1[k]==S2[k]:
            befoans+=1
        else:
            break
    for k in range(min(len(S3),len(S2))):
        if S2[k]==S3[k]:
            aftans+=1
        else:
            break
    idx=ss[i][1]
    #print(idx)
    lists[idx]=max(aftans,befoans)
befoans=0
S1=list(ss[0][0])
S2=list(ss[1][0])
for k in range(min(len(S1),len(S2))):
    if S1[k]==S2[k]:
        befoans+=1
    else:
        break
idx=ss[0][1]
lists[idx]=befoans
S1=list(ss[-1][0])
S2=list(ss[-2][0])
befoans=0
for k in range(min(len(S1),len(S2))):
    if S1[k]==S2[k]:
        befoans+=1
    else:
        break
idx=ss[-1][1]
lists[idx]=befoans
for i in lists:
    print(i)
        