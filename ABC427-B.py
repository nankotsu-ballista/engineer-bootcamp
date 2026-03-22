n=int(input())
A=[]
sums=1
for i in range(1,n):
    sumstr=str(sums)
    for k in range(len(sumstr)):
        sums+=int(sumstr[k])
print(sums)
