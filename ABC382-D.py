import sys

n, m = map(int, sys.stdin.read().split())

w = [[]]

for i in range(1, n + 1):
    v = []
    for a in w:
        start = 1 if i == 1 else a[-1] + 10
        end = m - 10 * (n - i)
        for x in range(start, end + 1):
            na = a + [x]
            v.append(na)
    w = v

X = len(w)
print(X)

for a in w:
   print(*a)