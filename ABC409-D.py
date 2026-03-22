def solve():
    N = int(input())
    S = input()

    # 辞書順が崩れる最初の位置を探す
    l = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            l = i
            break

    # 崩れてなければそのまま出力
    if l == -1:
        print(S)
        return

    # S[l] より大きい最初の文字位置 r を探す
    r = N
    for j in range(l + 1, N):
        if S[l] < S[j]:
            r = j
            break

    # 左巡回シフト後の文字列を構築
    rotated = S[:l] + S[l + 1:r] + S[l] + S[r:]
    print(rotated)

# 複数テストケース処理
T = int(input())
for _ in range(T):
    solve()
