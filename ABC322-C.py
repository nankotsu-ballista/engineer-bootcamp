N, M = map(int, input().split())
A = list(map(int, input().split()))

res = []
prev = 0

for day in A:
    length = day - prev
    for i in range(length):
        res.append(length - i - 1)
    prev = day

print('\n'.join(map(str, res)))
