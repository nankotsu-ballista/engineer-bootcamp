n=int(input())
s=list(str(n))
tmp=[]
for i in range(len(s)):
    tmp.append(int(s[i]))
ans=0
for ketawa in range(1,9*(len(s))+1):
    dp=[[[[0]*2 for _ in range(ketawa)]for _ in range(ketawa+1)]for _ in range(len(s)+1)]
    dp[0][0][0][1]=1
    for i in range(len(s)):
        for k in range(ketawa+1):
            for j in range(ketawa):
                for d in range(10):
                    if k+d>ketawa:
                        continue
                    if tmp[i]==d:
                        dp[i+1][k+d][(j*10+d)%ketawa][0]+=dp[i][k][j][0]
                        dp[i+1][k+d][(j*10+d)%ketawa][1]+=dp[i][k][j][1]
                    elif tmp[i]<d:
                        dp[i+1][k+d][(j*10+d)%ketawa][0]+=dp[i][k][j][0]
                    elif tmp[i]>d:
                        dp[i+1][k+d][(j*10+d)%ketawa][0]+=dp[i][k][j][0]
                        dp[i+1][k+d][(j*10+d)%ketawa][0]+=dp[i][k][j][1]
    ans+=dp[len(s)][ketawa][0][0]+dp[len(s)][ketawa][0][1]
print(ans)
            
