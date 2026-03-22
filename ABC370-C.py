s = list(input())
t = list(input())
n = len(s)
ans = []

# S[i] > T[i]（辞書順を小さくする）を前から
for i in range(n):
    if s[i] > t[i]:
        s[i] = t[i]
        ans.append("".join(s))

# S[i] < T[i]（辞書順を大きくする）を後ろから
for i in reversed(range(n)):
    if s[i] < t[i]:
        s[i] = t[i]
        ans.append("".join(s))

print(len(ans))
print("\n".join(ans))
