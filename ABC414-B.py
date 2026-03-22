N=int(input())
count=0
S=""
sum=0
for i in range(N):
    A,B=input().split()
    sum+=int(B)
    if sum > 100:
        print("Too Long")
        exit()
    for i in range(int(B)):
        S+=A
    
if len(S)<=100:
    print(S)