n=int(input())
s=""
for i in range(n,0,-1):
    if i==1:
        s=s+str(i)
    else:
        s=s+str(i)+","
print(s)