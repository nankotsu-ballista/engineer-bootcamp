def is_white(i, j):
    while i > 0 or j > 0:
        if i % 3 == 1 and j % 3 == 1:
            return True
        i //= 3
        j //= 3
    return False

N = int(input())
L = 3 ** N
for y in range(L):
    row = []
    for x in range(L):
        row.append("." if is_white(y, x) else "#")
    print("".join(row))