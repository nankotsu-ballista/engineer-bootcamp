T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    S=list(S)
    zeros=[]
    ones=[]
    zero=0
    one=0
    for i in range(N):
        if S[i]=="0":
            zero+=1
        else:
            one+=1
        zeros.append(zero)
        ones.append(one)
    #print(zeros)
    #print(ones)
    ans=0
    minidx=-1
    minvalue=0
    ans=10**10
    for i in range(N):
        temp=ones[i]-zeros[i]
        #print(temp)
        if temp<minvalue:
            minidx=i
            minvalue=temp
        ans=min(ans,(minvalue-(ones[i]-zeros[i])))
        #print(minvalue)
    print(ones[-1]+ans)
    
    
