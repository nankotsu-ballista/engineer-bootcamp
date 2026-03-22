K=int(input())
ans=[]
for i in range(2,1 << 10):
    x=0
    for j in range(9,-1,-1):
        if(i>>j) & 1:
            x = x*10+j
    ans.append(x)
ans.sort()

print(ans[K-1])