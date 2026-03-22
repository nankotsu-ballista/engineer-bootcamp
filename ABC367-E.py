import sys

it = iter(sys.stdin.buffer.read().split())
n = int(next(it)); K = int(next(it))
X = [0] + [int(next(it)) for _ in range(n)]   # 1-index
A = [0] + [int(next(it)) for _ in range(n)]   # 1-index

LOG = 60  # K <= 1e18 なので 60 で十分

# double[k][i] = i から 2^k 回進んだ先（転置）
double = [[0] * (n + 1) for _ in range(LOG)]
d0 = double[0]
for i in range(1, n + 1):
    d0[i] = X[i]

for k in range(LOG - 1):
    dk = double[k]
    dnk = double[k + 1]
    for i in range(1, n + 1):
        dnk[i] = dk[dk[i]]

# pos[i] = i から K 回進んだ先（全点一括）
pos = list(range(n + 1))
kk = K
bit = 0
while kk:
    if kk & 1:
        dk = double[bit]
        for i in range(1, n + 1):
            pos[i] = dk[pos[i]]
    kk >>= 1
    bit += 1

# 答えのAを拾う
out = [str(A[pos[i]]) for i in range(1, n + 1)]
sys.stdout.write(" ".join(out))