n = int(input())
s = input()

mx = [0] * 26  # a〜zの最大連続数

l = 0
while l < n:
    r = l + 1
    while r < n and s[l] == s[r]:
        r += 1
    c = ord(s[l]) - ord('a')
    mx[c] = max(mx[c], r - l)
    l = r

print(sum(mx))