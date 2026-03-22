n=int(input())
s=input()
ans=0
count=0
for i in range(n):
    if s[i]=="o":
        count+=1
    else:
        ans=max(count,ans)
        count=0
ans=max(count,ans)
if ans==n or ans==0:
    print(-1)
else:
    print(ans)