# N,M=map(int,input().split())
# A=list(map(int,input().split()))
N=int(input())
headmax=0
sum=0
for i in range(N):
    A,B=map(int,input().split())
    if B-A > headmax:
        headmax=B-A
        idx=i
    sum+=A
print(sum+headmax)

    