N=int(input())
A = list(map(int, input().split()))
goukei=sum(A)
heikin=goukei//N
amari=goukei-N*heikin
A.sort()
B=[heikin]*N
summer=0
for i in range(amari):
    B[N-i-1] +=1
for i in range(N):
    summer += abs(B[i]-A[i])
print(summer//2)