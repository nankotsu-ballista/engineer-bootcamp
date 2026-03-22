s=list(map(int,input().strip()))
numsodd=[0]*10
them=[]
counters=[0]*(2**10+1)
counters[0]+=1
for i in range(len(s)):
    numsodd[s[i]]=(numsodd[s[i]]+1)%2
    #print(numsodd)
    sum=0
    for i in range(len(numsodd)):
        sum+=2**i*numsodd[i]
    counters[sum]+=1
#print(counters)
ans=0
for i in range(len(counters)):
    if counters[i]!=0:
        ans+=counters[i]*(counters[i]-1)//2
print(ans)
        
    