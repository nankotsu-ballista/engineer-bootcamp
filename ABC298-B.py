n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
B=[list(map(int,input().split())) for _ in range(n)]
bset=set()
for i in range(n):
    for k in range(n):
        if A[i][k]==1:
            bset.add((i+1,k+1))
tmp=set()
for i in range(n):
    for k in range(n):
        if B[i][k]==1:
            tmp.add((i+1,k+1))
#print(tmp)
tmp1=set()
tmp2=set()
tmp3=set()
tmp4=set()
#print(bset)

for cc in tmp:
    x,y=cc
    tmp1.add((n-y+1,x))
for cc in tmp1:
    x,y=cc
    tmp2.add((n-y+1,x))
for cc in tmp2:
    x,y=cc
    tmp3.add((n-y+1,x))
for cc in tmp3:
    x,y=cc
    tmp4.add((n-y+1,x))
# print(bset)
# print(tmp1)
# print(tmp2)
# print(tmp3)
# print(tmp4)
check=True
for i in bset:
    x,y=i
    if (x,y) in tmp1:
        continue
    else:
        check=False
        break
if check==True:
    print("Yes")
    exit()
check=True    
for i in bset:
    x,y=i
    if (x,y) in tmp2:
        continue
    else:
        check=False
        break
if check==True:
    print("Yes")
    exit()
check=True    
for i in bset:
    x,y=i
    if (x,y) in tmp3:
        continue
    else:
        check=False
        break
if check==True:
    print("Yes")
    exit()
check=True    
for i in bset:
    x,y=i
    if (x,y) in tmp4:
        continue
    else:
        check=False
        break
if check==True:
    print("Yes")
    exit()

print("No")


    
            