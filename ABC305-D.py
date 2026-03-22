import sys
import bisect

input = sys.stdin.readline

# 入力
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [tuple(map(int, input().split())) for _ in range(Q)]

# 1. 寝ていた時間の累積和（sleep_sum[i] = A[i]までに寝た合計時間）
sleep_sum = [0] * N
for i in range(1, N, 2):  # 奇数index（就寝時間）
    sleep_sum[i] = sleep_sum[i - 1]
    sleep_sum[i + 1] = sleep_sum[i] + (A[i + 1] - A[i])
# 奇数以外も補完
for i in range(1, N):
    sleep_sum[i] = max(sleep_sum[i], sleep_sum[i - 1])

# 2. f(x): xまでに寝た時間
def f(x):
    i = bisect.bisect_right(A, x) - 1
    if i < 0:
        return 0
    res = sleep_sum[i]
    # もし x が「寝ている区間」内なら補間追加
    if i % 2 == 1:  # iが奇数（寝始めた瞬間 or 以降）
        res += x - A[i]
    return res

# 3. クエリ処理
for l, r in LR:
    print(f(r) - f(l))
