# a = int(input())
# スペース区切りの整数の入力
a,b = map(int, input().split())
# 文字列の入力
r = a * b % 2
if r == 1:
  print("Odd")
else:
  print("Even")
