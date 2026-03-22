n=int(input())
nodes=[[-1]*n for _ in range(n)]
for i in range(n-1):
    c=list(map(int,input().split()))
    for k in range(len(c)):
        nodes[i][i+k+1]=c[k]
#print(nodes)
for i in range(n):
    for k in range(i+1,n):
        for j in range(i+1,k):
            if nodes[i][k]>nodes[i][j]+nodes[j][k]:
                print("Yes")
                exit()
print("No")