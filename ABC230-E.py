n=int(input())
# while n!=0:
#     beforen=n
#     n=n//2+1
#     print(beforen,n)
#     ans+=(first//beforen)*(beforen-n+1)
#     #print(first//beforen,first//n)
#     n-=1
# print(ans)

num=n
first=num
beforen=num
ans=0
while num!=1:
    left=0
    right=num
    nxt=first//num
    while left<right:
        mid=(left+right)//2
        if first//mid<=nxt:
            right=mid
        else:
            left=mid+1
    #print(beforen,left,nxt)
    ans+=(beforen-left+1)*nxt
    num=left-1
    beforen=num
print(ans+first)
