n,q=map(int,input().split())
minimum=0
PCcount=[0]
for i in range(n):
    PCcount.append(1)
#print(PCcount)
for i in range(q):
    x,y=map(int,input().split())
    sum=0
    if x<minimum:
        print(0)
    else:    
        for k in range(minimum,x+1):
            sum+=PCcount[k]
            PCcount[k]=0
        minimum=x
        PCcount[y]+=sum
        print(sum)
    #print(PCcount)
    #print(x,y,minimum)
            