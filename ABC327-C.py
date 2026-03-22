grid=[input().split() for _ in range(9)]
#print(grid)
for k in range(9):
    for i in range(9):
        for j in range(i+1,9):
            if grid[k][i]==grid[k][j]:
                print("No")
                exit()
for k in range(9):
    for i in range(9):
        for j in range(i+1,9):
            if grid[i][k]==grid[j][k]:
                print("No")
                exit()
def box(il,jl):
    numbers=[0]*(9)
    for k in range(3):
        for l in range(3):
            numbers[int(grid[3*il+k][3*jl+l])-1]+=1
    for q in range(9):
        if numbers[q]!=1:
            return False
    return True
for i1 in range(3):
    for j1 in range(3):
        if not box(i1, j1):
            print("No")
            exit()
print("Yes")
            
            