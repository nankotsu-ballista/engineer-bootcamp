point = list(map(int,input().split()))
point = [-p for p in point]

standings=[]
for bit in range(1,32):
    solved_point=0
    name=""
    for digit in range(5):
        if bit & 1<<digit:
            solved_point += point[digit]
            name += "ABCDE"[digit]
            
    standings.append((solved_point,name))

for _, name in sorted(standings):
    print(name)