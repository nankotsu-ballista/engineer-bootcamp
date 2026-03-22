n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
total=0
for i in range(n):
    total+=min(a[i],b[i])
#print(total)
    
tempo=0
tempoafter=0
for i in range(q):
    t,p,l=map(str,input().split())
    if t=="A":
        tempo=min(a[int(p)-1],b[int(p)-1])
        a[int(p)-1]=int(l)
        tempoafter=min(a[int(p)-1],b[int(p)-1])
        total=total-tempo+tempoafter
        print(total)
    else:
        tempo=min(a[int(p)-1],b[int(p)-1])
        b[int(p)-1]=int(l)
        tempoafter=min(a[int(p)-1],b[int(p)-1])
        total=total-tempo+tempoafter
        print(total)
    
# print(a)
# print(b)