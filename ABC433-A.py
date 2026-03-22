x,y,z=map(int,input().split())
for i in range(1000):
    if x+i==z*(y+i):
        print("Yes")
        exit()
print("No")