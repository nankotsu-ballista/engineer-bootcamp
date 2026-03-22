n=int(input())
p=list(map(int,input().split()))
t=[]
for i in range(n-1):
    if p[i]<p[i+1]:
        t.append("<")
    else:
        t.append(">")
count=0
#print(t)
pop=[]
for i in t:
    if i =="<":
        count+=1
    else:
        if count!= 0:
            pop.append(count)
        count=0
if count!= 0:
    pop.append(count)
#print(pop)
sum=0
for i in range(len(pop)-1):
    sum+=(int(pop[i])*int(pop[i+1]))
print(sum)
    
    
    