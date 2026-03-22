from collections import deque
a,b,c= map(int,input().split())
#S = [list(input()) for _ in range(H)]
dice=[0]*7
dice[a]+=1
dice[b]+=1
dice[c]+=1
if max(dice)== 2:
    for i in range(7):
        if dice[i] ==1:
            print(i)
elif max(dice)== 3:
    for i in range(7):
        if dice[i] ==3:
            print(i)
else:        
    print(0)