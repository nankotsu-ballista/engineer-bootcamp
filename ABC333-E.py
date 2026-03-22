n=int(input())
c=[]
for i in range(n):
    t,x=map(int,input().split())
    c.append((t,x))
#print(c)
c.reverse()
#print(c)
monsters=[0]*(n+1)
ans=-1
count=0
use=[]
for i in range(n):
    t,x=c[i]
    if t == 1:
        if monsters[x]!=0:
            monsters[x]-=1
            count-=1
            use.append(1)
        else:
            use.append(0)
        ans=max(count,ans)
    else:
        monsters[x]+=1
        count+=1
        ans=max(count,ans)
if count!=0:
    print(-1)
else:
    print(ans)
    use.reverse()
    # print(use)
    print(*use)