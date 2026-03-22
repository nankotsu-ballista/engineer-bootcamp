N=int(input())
A=list(map(int,input().split()))
setter=[-1]*(N+1)
#print(setter)
ans=0
length=0
left=0
for i in range(N//2):
    if A[2*i]==A[2*i+1]:
        if setter[A[2*i]]!=-1:
            ans=max(length,ans)
            if left<=setter[A[2*i]]:
                    left=setter[A[2*i]]+1
                    length=i-left+1
            else:
                length+=1
        else:
            length+=1
        setter[A[2*i]]=i
    else:
        left=i
        ans=max(length,ans)
        length=0
    # print(setter)
    # print(length,left)
ans=max(length,ans)
length=0
setter=[-1]*(N+1)
left=0
for i in range(N//2):
    if i*2+2<N:
        if A[2*i+1]==A[2*i+2]:
            if setter[A[2*i+1]]!=-1:
                ans=max(length,ans)
                if left<=setter[A[2*i+1]]:
                    left=setter[A[2*i+1]]+1
                    length=i-left+1
                else:
                    length+=1
                #print("a")
            else:
                length+=1
                #print("b")
            setter[A[2*i+1]]=i
        else:
            ans=max(length,ans)
            left=i
            length=0
        #     print("c")
        # print(length)
        # print(i)
ans=max(length,ans)
print(ans*2)
#print(setter)
        