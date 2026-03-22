N = int(input())
S = list(input())  # ← ★文字列Sをリストに
Q = int(input())

alphabet = [None] * N  # Noneで初期化（未変更状態）
alphabettime = [-1] * N
lastpie = -1
lastodd = -1

for i in range(Q):
    A, B, C = input().split()
    B = int(B) - 1  # ★問題で1-indexなら0-indexに調整

    if A == "1":
        alphabet[B] = C
        alphabettime[B] = i
    elif A == "2":
        lastodd = i
    elif A == "3":
        lastpie = i

# 各文字への更新
for i in range(N):
    if alphabet[i] is not None:
        S[i] = alphabet[i]

# 小文字 or 大文字化（更新タイムスタンプを見て）
if lastpie < lastodd:
    for i in range(N):
        if alphabettime[i] < lastodd:
            S[i] = S[i].lower()
else:
    for i in range(N):
        if alphabettime[i] < lastpie:
            S[i] = S[i].upper()

print(''.join(S))
