N=int(input())
A=input().split()
X=input()
count = 0
for i in range(0,N):
  if A[i]==X:
    count = 1
    
if count == 1:
  print("Yes")
else:
  print("No")