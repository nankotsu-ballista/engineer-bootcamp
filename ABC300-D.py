n=int(input())
q=n**(1/2)
q=int(q)
sosuu=[2]
for i in range(3,q):
    check=True
    for j in sosuu:
        if j*j>i:
            break
        if i%j==0:
            check=False
            break
    if check == True:
        sosuu.append(i)
count=len(sosuu)
ans=0
k=count-1
for i in range(count-2):
    if i>=k:
            break
    k=count-1
    for j in range(i+1,count):
        if j>=k:
            break
        while j<k:
            if(sosuu[i]**2*sosuu[j]*sosuu[k]**2)>n:
                k-=1
            else:
                break
        ans+=(k-j)
                
print(ans)
