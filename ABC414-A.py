N,L,R=map(int,input().split())
count=0
for i in range(N):
    A,B=map(int,input().split())
    if A<=L and B>=R:
        count+=1
print(count)