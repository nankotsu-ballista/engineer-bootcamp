n=int(input())
normal = set()
negated = set()

for _ in range(n):
  s = input()
  if s.startswith("!"):
    negated.add(s[1:])
  else:
    normal.add(s)
  
for word in normal:
  if word in negated:
    print(word)
    exit()

print("satisfiable")
  