n,k=map(int,input().split())
A=list(map(int,input().split()))
if len(A)==1:
    print(0)
    exit()
if len(A)%2==1:
    sum=0
    left=[]
    left.append(sum)
    for i in range(len(A)//2):
        s=A[2*i+1]-A[2*i]
        sum+=s
        left.append(sum)
        left.append(sum)
    #print(left)
    right=[]
    sum=0
    right.append(sum)
    for i in range(len(A)//2,0,-1):
        s=A[2*i]-A[2*i-1]
        #print(2*i)
        sum+=s
        right.append(sum)
        right.append(sum)
    right.reverse()
    #print(right)
    ans=10**18
    for i in range(k):
        if i%2==1:
            continue
        ans=min(ans,right[i]+left[i])
else:
    sum=0
    for i in range(len(A)//2):
        s=A[2*i+1]-A[2*i]
        sum+=s
    ans=sum
print(ans)