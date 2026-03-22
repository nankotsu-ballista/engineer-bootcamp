S=str(input())
N=int(input())
S=list(S)
S=S[::-1]
sum=0
adjust=[]
for i in range(len(S)):
    if S[i]=="1":
        sum+=2**(i)
    elif S[i]=="?":
        adjust.append(2**(i))
adjust=adjust[::-1]
if sum>N:
    print(-1)
    exit()
else:
    for j in adjust:
        if j+sum <= N:
            sum+=j
print(sum)
    