def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def to_base(x: int, base: int) -> str:
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res if res else '0'

def solve(A: int, N: int) -> int:
    total = 0
    i = 1

    while True:
        # 奇数桁の回文（例: 12321）
        s = str(i)
        p1 = int(s + s[-2::-1])
        if p1 > N:
            break
        if is_palindrome(to_base(p1, A)):
            total += p1

        # 偶数桁の回文（例: 1221）
        p2 = int(s + s[::-1])
        if p2 <= N and is_palindrome(to_base(p2, A)):
            total += p2

        i += 1

    return total

# 入力
A = int(input())
N = int(input())
print(solve(A, N))