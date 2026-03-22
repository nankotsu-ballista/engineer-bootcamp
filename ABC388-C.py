import bisect
n=int(input())
setter=[]
a=list(map(int,input().split()))
for i in range(n):
    setter.append(a[i])
setter=list(setter)
#print(setter)
ans=0
for i in range(len(setter)):
    su=bisect.bisect_right(a, setter[i]//2)
    ans+=su
print(ans)

        
    