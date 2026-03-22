from collections import deque
n,x=map(int,input().split())
one=[]
two=[]
three=[]
for _ in range(n):
    v,a,c=map(int,input().split())
    if v==1:
        one.append((a,c))
    elif v==2:
        two.append((a,c))
    elif v==3:
        three.append((a,c))
dpone=[[0]*5001 for _ in range(len(one)+1)]
dptwo=[[0]*5001 for _ in range(len(two)+1)]
dpthree=[[0]*5001 for _ in range(len(three)+1)]
for i in range(len(one)):
    amount,colorie=one[i]
    for k in range(5001):
        if k>=colorie:
            dpone[i+1][k]=max(dpone[i][k],dpone[i][k-colorie]+amount)
        else:
            dpone[i+1][k]=dpone[i][k]
for i in range(len(two)):
    amount,colorie=two[i]
    for k in range(5001):
        if k>=colorie:
            dptwo[i+1][k]=max(dptwo[i][k],dptwo[i][k-colorie]+amount)
        else:
            dptwo[i+1][k]=dptwo[i][k]
for i in range(len(three)):
    amount,colorie=three[i]
    for k in range(5001):
        if k>=colorie:
            dpthree[i+1][k]=max(dpthree[i][k],dpthree[i][k-colorie]+amount)
        else:
            dpthree[i+1][k]=dpthree[i][k]
# print(dpone[-1][:20])
# print(dptwo[-1][:20])
# print(dpthree[-1][:20])
vitamins=[[0,1,0],[0,2,0],[0,3,0]]
for i in range(x):
    vitamins.sort()
    #print(vitamins)
    vitamins[0][2]+=1
    if vitamins[0][1]==1:
        vitamins[0][0]=dpone[-1][vitamins[0][2]]
    elif vitamins[0][1]==2:
        vitamins[0][0]=dptwo[-1][vitamins[0][2]]
    elif vitamins[0][1]==3:
        vitamins[0][0]=dpthree[-1][vitamins[0][2]]
print(min(vitamins[0][0],vitamins[1][0],vitamins[2][0]))
    
            
            
        



    

    