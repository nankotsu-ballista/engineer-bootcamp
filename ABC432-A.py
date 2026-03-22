a,b,c=map(int,input().split())
anss=[a,b,c]
anss.sort()
anss.reverse()
ans=""
for i in anss:
    ans=ans+str(i)
print("".join(ans))