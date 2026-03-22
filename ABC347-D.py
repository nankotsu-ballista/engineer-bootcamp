from collections import deque
a,b,C=map(int,input().split())
C=str(bin(C))
C=C[2:]
C=list(C)
C.reverse()
for i in range(len(C),60):
    C.append("0")
C.reverse()
count=0
pos=[]
for i in range(len(C)):
    if C[i]=="1":
        count+=1
        pos.append(i)
# print(pos)
# print(count)
l=abs(a-b)
if a+b>=60:
    r=120-a-b
else:
    r=a+b
#print(l,r,count)
if(a - b + count)%2==1:
    print(-1)
    exit()
if not (l<=count<=r):
    print(-1)
    exit()
A=[0]*60
B=[0]*60
last=-1
if a<b:
    for i in range(b-a):
        A[pos[i]]=0
        B[pos[i]]=1
        last=i
else:
    for i in range(a-b):
        A[pos[i]]=1
        B[pos[i]]=0
        last=i
cnt=0
check=True

for i in range(last+1,len(pos)):
    if check==False:
        A[pos[i]]=0
        B[pos[i]]=1
        check=True
    else:
        A[pos[i]]=1
        B[pos[i]]=0
        check=False
cnt=0
for i in A:
    if i==1:
        cnt+=1
#print(cnt)
ct=0
for i in range(len(A)):
    if ct==(a-cnt):
        break
    if A[i] == 0 and B[i]==0:
        A[i]=1
        B[i]=1
        ct+=1
ansA=0
ansB=0
# print(A)
# print(B)
sA = ''.join(map(str, A))
sB = ''.join(map(str, B))
sC = ''.join(map(str, C))
#print(sC)
# print(sA)
# print(sB)
le=len(A)
for i in range(le):
    if A[i]==1:
        ansA+=2**(le-i-1)
    if B[i]==1:
        ansB+=2**(le-i-1)
print(int(sA, 2),int(sB, 2))
cnt=0
cnt=0
for i in B:
    if i==1:
        cnt+=1
#print(cnt)
    


    
    
        
    