n,d=map(int,input().split())
T=list(map(int,input().split()))
for i in range(n-1):
    if T[i+1]-T[i]<=d:
        print(T[i+1])
        exit()
print(-1)