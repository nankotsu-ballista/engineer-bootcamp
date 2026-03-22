N, M, H, K = map(int, input().split())
S=input()
items = set()
for _ in range(M):
    x, y = map(int, input().split())
    items.add((x, y))
posix=0
posiy=0
health=H
for i in range(N):
    health -= 1
    if S[i] == "R":
        posix += 1
    elif S[i] == "L":
        posix -= 1
    elif S[i] == "U":
        posiy += 1
    elif S[i] == "D":
        posiy -= 1
    if health< 0:
        print("No")
        exit()    
    if health<K and  (posix, posiy) in items:
        health = K
        items.remove((posix,posiy))
    
    #print(health)
    #print(posix)
    #print(posiy)
        
print("Yes")