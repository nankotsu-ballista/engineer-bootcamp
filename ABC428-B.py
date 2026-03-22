anss=[]
n,k=map(int,input().split())
s=input()
for i in range(n-k+1):
    c=s[i:i+k]
    #print(c)
    count=0
    for j in range(n-k+1):
        q=s[j:j+k]
        if q==c:
            count+=1
    anss.append((count,c))
anss.sort(reverse=True)
#print(anss)
s=set()
maxcount=anss[0][0]
#print(maxcount)
for i in range(len(anss)):
    if anss[i][0]==maxcount and anss[i][1] not in s:
        s.add(anss[i][1])
#print(s)
s=list(s)
s.sort()
print(maxcount)
print(*s)

    
        