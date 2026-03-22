nn=int(input())
n=int(nn**(0.5)//1)
a = [True] * (n + 1)
a[0] = a[1] = False

p = 2
while p * p <= n:
    if a[p]:
        i = p * p
        while i <= n:
            a[i] = False
            i += p
    p += 1
q=0
t=[]
for i in range(n + 1):
    if a[i]:
        t.append(i)
#print(len(t))
ans=0
#print(t)
c=0
if t:
    c=100
else:
    print(0)
    exit()
for i in range(len(t)):
    for k in range(i+1,len(t)):
        if t[i]**2*t[k]**2<=nn:
           # print(t[i],t[k])
            ans+=1
        else:
            break
for i in range(100):
    if t[i]**8>nn:
        break
    else:
        ans+=1
print(ans)
        