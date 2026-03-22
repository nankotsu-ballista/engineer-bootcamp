import bisect

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

# 累積和
check = [0] * N
check[0] = P[0]
for i in range(1, N):
    check[i] = check[i - 1] + P[i]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    start = bisect.bisect_left(X, L)
    end = bisect.bisect_right(X, R)  # ← bisect_leftだと Rピッタリが入らないので rightに変更

    if start >= end:
        print(0)
        continue

    if start == 0:
        ans = check[end - 1]
    else:
        ans = check[end - 1] - check[start - 1]
    print(ans)
