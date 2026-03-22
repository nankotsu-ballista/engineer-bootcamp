n=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(n):
    B.append(A[i])
A.sort()
value=A[-2]
#print(value)
for i in range(n):
    if B[i]==value:
        print(i+1)