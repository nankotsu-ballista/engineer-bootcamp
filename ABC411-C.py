N, Q = map(int, input().split())
A = list(map(int, input().split()))
check = [0] * (N + 2)
count = 0

for i in range(Q):
    if check[A[i]] == 0:
        check[A[i]] = 1
        if check[A[i]+1] + check[A[i]-1] == 2:
            count -= 1
        elif check[A[i]+1] + check[A[i]-1] == 0:
            count += 1
    else:
        check[A[i]] = 0
        if check[A[i]+1] + check[A[i]-1] == 2:
            count += 1
        elif check[A[i]+1] + check[A[i]-1] == 0:
            count -= 1
    print(count)
#print(check)