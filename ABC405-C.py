N=int(input())
A=input().split()
sum= 0
sum2= 0
for i in range(0,N):
  sum=sum+int(A[i])
  sum2=sum2+int(A[i])*int(A[i])

tla=(sum*sum-sum2)//2
print(tla)