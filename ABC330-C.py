import math

D = int(input())

min_diff = float('inf')
ans_x = ans_y = 0

for x in range(int(math.isqrt(D)) + 2):  # ceil(√D) でもOK
    C = x * x - D
    if C >= 0:
        y = 0
        diff = abs(x * x + y * y - D)
        if diff < min_diff:
            min_diff = diff
            ans_x, ans_y = x, y
    else:
        target = -C
        y1 = int(math.sqrt(target))
        for y in [y1, y1 + 1]:
            diff = abs(x * x + y * y - D)
            if diff < min_diff:
                min_diff = diff
                ans_x, ans_y = x, y

print(min_diff)