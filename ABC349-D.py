l,r=map(int,input().split())
i=0
t=[]
while l<r:
    i=0
    while l%2**(i+1)==0 and (2**(i+1)+l)<=r:
        i+=1
    t.append((l,(2**i)+l))
    l=(2**i)+l
#print(t)
print(len(t))
for ll,rr in t:
    print(ll,rr)