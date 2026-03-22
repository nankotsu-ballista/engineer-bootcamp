N, Q = map(int, input().split())
A = list(range(1, N + 1))
offset = 0

for _ in range(Q):
    query = input().split()
    typ = int(query[0])

    if typ == 1:
        p, x = int(query[1]), int(query[2])
        A[(p - 1 + offset) % N] = x

    elif typ == 2:
        p = int(query[1])
        print(A[(p - 1 + offset) % N])

    else:
        k = int(query[1])
        offset = (offset + k) % N
