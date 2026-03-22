from collections import deque
a,b,c,d=map(int,input().split())
s=set()
for i in range(2,201):
    s.add(i)
for i in range(2,201):
    for k in range(2,21):
        if i%k==0 and i!=k:
            s.discard(i)
#print(s)
for i in range(a,b+1):
    check=True
    for k in range(c,d+1):
        if i+k in s:
            check=False
            break
    if check==True:
        print("Takahashi")
        exit()
print("Aoki")
        
            