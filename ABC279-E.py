n,m=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in range(1,n+1):
    B.append(i)
#print(B)
pos=[]
for i in range(m):
    B[A[i]-1],B[A[i]]=B[A[i]],B[A[i]-1]
    if B[A[i]-1]==1:
        pos.append(B[A[i]])
    elif B[A[i]]==1:
        pos.append(B[A[i]-1])
    else:
        pos.append(1)
    #print(B)
#print(pos)
pospos=[-1]*(n+1)
B=[0]+B
for i in range(1,n+1):
    pospos[B[i]]=i
#print(pospos)
for i in pos:
    print(pospos[i])
        