n=int(input())
b=10**6+1
ans=10**18+1
for a in range(0,10**6+1):
    while b>-2:
        if a**3+(a**2)*b+a*(b**2)+b**3>=n:
          if b>=0:
            ans=min(ans,a**3+(a**2)*b+a*(b**2)+b**3)
          b-=1
        else:
            b+=1
            #print(a,b)
            break
if ans==10**18+1:
    print(0)
else:
    print(ans)