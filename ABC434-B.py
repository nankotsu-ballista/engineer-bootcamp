n,m=map(int,input().split())
birds=[[]for _ in range(m+1)]
for i in range(n):
    a,b=map(int,input().split())
    birds[a].append(b)
#print(birds)
for i in range(1,m+1):
    print(sum(birds[i])/len(birds[i]))