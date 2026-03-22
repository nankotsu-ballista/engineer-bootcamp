from collections import deque
n, q = map(int, input().split())
Q = [list(input().split()) for _ in range(q)]
head=[1,0]
x=[0]*(10**6)
y=[0]*(10**6)
count=0
x[0]=1
for i in range(q):
    temp=Q[i]
    if temp[0]== "1":
        if temp[1]=="U":
            head[1]+=1
        elif temp[1]=="R":
            head[0]+=1
        elif temp[1]=="D":
            head[1]-=1
        elif temp[1]=="L":
            head[0]-=1
        #print(count)
        count=count+1
        x[count]=head[0]
        y[count]=head[1]
    else:
        if int(temp[1])-count > 0:
            #print("case1 "+str(int(temp[1])-count)+" 0")
            print(str(int(temp[1])-count)+" 0")
        else:
            #print("case2 "+str(x[count-int(temp[1])+1])+" "+str(y[count-int(temp[1])+1]))
            print(str(x[count-int(temp[1])+1])+" "+str(y[count-int(temp[1])+1]))
            
#print(y)

    