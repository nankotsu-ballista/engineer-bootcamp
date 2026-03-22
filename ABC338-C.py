N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
inf = 10**18

ans= 0
for x in range(max(Q)+1):
    y= inf
    for i in range(N):
        if Q[i] < A[i] * x:
            y= -inf
        elif B[i] > 0:
            y=min(y,(Q[i]-A[i] * x)//B[i])
    ans = max(ans,x+y)
print(ans)