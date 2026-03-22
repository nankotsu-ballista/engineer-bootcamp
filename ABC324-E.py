n,t=map(str,input().split())
n=int(n)
wilds=0
forward=[]
back=[0]*(2*10**6+1)
backset=[-1]*(2*10**6+1)
for i in range(n):
    s=input()
    count=0
    idx=0
    for k in s:
        if idx < len(t) and k == t[idx]: 
            count+=1
            idx+=1
        if idx==len(t):
            break
    forward.append((count,i))
    count=0
    idx=len(t)-1
    for k in range(len(s)):
        if idx >= 0 and s[-k-1] == t[idx]:
            count+=1
            idx-=1
            if idx < 0:
                break
    back[count]+=1
    backset[i]=count
sum=0
for i in range(2*10**6,-1,-1):
    sum+=back[i]
    back[i]=sum
# print(back[:10])
# print(forward)
ans=0
for i in range(len(forward)):
    count,idx=forward[i]
    if len(t)-count<backset[i]:
        ans+=back[len(t)-count]
    else:
        ans+=back[len(t)-count]
#print(wilds)
print(ans)
