n=int(input())
A=list(map(int,input().split()))
s=set()
check=True
new=[0]*n
#print(new)

for i in range(len(A)):
    if A[i]==-1:
        continue
    else:
        if A[i] in s:
            check=False
        if A[i]<1 or A[i]>n:
            check=False
        s.add(A[i])
        new[i]=A[i]
#print(new)
t=[]
if check == False:
    print("No")
    exit()
else:
    for i in range(1,n+1):
        if i in s:
            continue
        else:
            t.append(i)
#print(t)
for i in range(n):
    if new[i]==0:
        new[i]=t.pop()
#print(new)
print("Yes")
for i in new:
    print(i, end=" ")
    
            
    