from collections import defaultdict
import heapq
q = defaultdict(int) 
n=int(input())
for i in range(n):
    size,slime=map(int,input().split())
    while size%2==0:
        size=size//2
        slime=slime*2
    q[size]+=slime
#print(q)
sum=0
for i in q.values():
    count=0
    i=int(i)
    st=str(bin(i))              # '0b11010'
    for j in range(len(st)):      # '11010'
        if st[j]=="1":
            count+=1
    #print(st)
    sum+=count
print(sum)

        
        
    
    
    