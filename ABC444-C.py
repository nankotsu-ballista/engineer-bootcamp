from collections import deque
n=int(input())
A=list(map(int,input().split()))
A.sort()
ans=[]
check=True
if n%2==0:
    for i in range(n//2):
        if A[i]+A[n-1-i]==A[0]+A[-1]:
            continue
        else:
            check=False
if n%2==1:
    # for i in range(n//2):
    #     if A[i]+A[n-1-i]==A[0]+A[-1]:
    #         continue
    #     else:
    #         check=False
    # if (A[n//2]*2)!=A[0]+A[-1]:
    check=False
q=deque()
maxi=max(A)
#print(maxi)
check2=True
for i in range(n):
    if maxi!=A[i]:
        q.append(A[i])
newlist=[]
while q:
    v=q.popleft()
    newlist.append(v)
#print(newlist)
if len(newlist)%2==1:
    check2=False
else:
    for i in range(len(newlist)//2):
        if newlist[i]+newlist[len(newlist)-1-i]==maxi:
            continue
        else:
            check2=False
            
            
            

if check2==True:
    ans.append(maxi)
if check==True:
    ans.append(A[0]+A[-1])
print(*ans)


    
    
