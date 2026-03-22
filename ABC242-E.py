q=int(input())
for _ in range(q):
    n=int(input())
    S=list(input())
    middle=0
    plus=0
    if n%2==1:
        middle=ord(S[n//2])-64
    mod=998244353
    S1=S[:n//2]
    if n%2==1:
        S2=S[n//2+1:]
    else:
        S2=S[n//2:]
    S1.reverse()
    #print(S1,S2)
    check=False
    for i in range(n//2):
        #print(S[i])
        #print(S[-(n//2)+i])
        if ord(S1[i])==ord(S2[i]):
            continue
        if ord(S1[i])>ord(S2[i]):
            plus=0
            check=True
            break
        if ord(S1[i])<ord(S2[i]):
            plus=1
            check=True
            break
    if check==False:
        plus=1
    if n%2==1:
        naga=n//2+1
    else:
        naga=n//2
    #print("plus",plus)
    #print("middle",middle)
    ans=1
    twsix=[]
    for i in range(naga):
        twsix.append(ans)
        ans*=26
        ans=ans%mod
    twsix.reverse()
    #print("twsix",twsix)
    ans=0
    
    for i in range(naga):
        ans=ans+(ord(S[i])-65)*twsix[i]
        ans=ans%mod
    print((ans+plus)%mod)
