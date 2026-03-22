n=int(input())
a,b,c=map(int,input().split())
ans=10**5
for i in range(10000):
    for k in range(10000-i):
      if (n-(b*i+c*k))<0:
        continue
      if (n-(b*i+c*k))%a==0:
        ans=min(ans,i+k+(n-(b*i+c*k))//a)
print(ans)
