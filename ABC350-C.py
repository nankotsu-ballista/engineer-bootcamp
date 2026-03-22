n = int(input())
A = list(map(int, input().split()))
idxlist = [0] * n
for i in range(n):
    idxlist[A[i] - 1] = i  # 値 i+1 の現在位置を記録

ops = []

for i in range(n):
    if idxlist[i] == i:
        continue
    swap_to = idxlist[i]
    A[i], A[swap_to] = A[swap_to], A[i]
    idxlist[A[swap_to] - 1] = swap_to
    idxlist[A[i] - 1] = i
    ops.append((i + 1, swap_to + 1))

print(len(ops))
for i, j in ops:
    print(i, j)