from string import ascii_lowercase
N = int(input())
S = input()
Q = int(input())
# 変換前と変換後の文字列を作る
# 'abcdefghijklmnopqrstuvwxyz' で初期化
mapping_from = ascii_lowercase
mapping_to = ascii_lowercase
for _ in range(Q):
    c, d = input().split()
    mapping_to = mapping_to.replace(c, d) # c を d に置き換える
# 対応する文字をそれぞれ置き換える
print(S.translate(str.maketrans(mapping_from, mapping_to)))
