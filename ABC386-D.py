from collections import defaultdict
N,M=map(int,input().split())
gyou=defaultdict(list)
#print(gyou)
for i in range(M):
    Y,X,C=map(str,input().split())
    Y=int(Y)
    X=int(X)
    gyou[Y].append((X,C))
#print(gyou)
for i in gyou:
    gyou[i].sort()
#print(gyou)
leftlimit=0
for i in sorted(gyou.keys(), reverse=True):
    check=False
    for k in range(len(gyou[i])):
        X,color=gyou[i][k]
        if color == "W" and X<=leftlimit:
            print("No")
            exit()
        if color =="W":
            check=True
        if check==True and color =="B":
            print("No")
            exit()
        if color == "B":
            leftlimit=X
print("Yes")
        


        
    
    
    