def main():
    r = int(input())

    def inside(a, b):
        return (2 * a + 1) ** 2 + (2 * b + 1) ** 2 <= 4 * r * r

    cnt = 0
    up = r - 1
    res = (r - 1) * 4 + 1

    x = 1
    while inside(x, 1):
        while not inside(x, up):
            up -= 1
        cnt += up
        x += 1

    res += cnt * 4
    print(res)

main()