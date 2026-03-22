import bisect

#N, M, D = map(int, input().split())
N=int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
maximum=[-1]*(10**6)
sum=[0]*(10**6)
check=[0]*(10**6)
for i in range(N):
    maximum[A[i]]=max(maximum[A[i]],W[i])
    sum[A[i]]+=W[i]
    check[A[i]] += 1
finalsum=0
for i in range(10**6):
    if check[i] >= 2:
        finalsum+=(sum[i]-maximum[i])
#print(maximum[0:40])
print(finalsum)
#print(sum[0:40])
#print(check[0:40])