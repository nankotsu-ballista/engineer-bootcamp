MOD = 998244353
n=int(input())
s=list(input())
dp =[[0]*10 for _ in range(2**10)]
for ch in s:
    x = ord(ch) - ord('A')                
    ndp =[row[:] for row in dp]
    bit = 1<<x
    for mask in range(1<<10):
        for last in range(10):
            v = dp[mask][last]
            if v == 0:
                continue
            if last == x:
                ndp[mask][last] = (ndp[mask][last]+v)%MOD
            else:
                if (mask&bit)==0:
                    ndp[mask|bit][x]=(ndp[mask|bit][x]+v) % MOD
    ndp[bit][x]=(ndp[bit][x] + 1) % MOD
    dp=ndp
ans=0
for mask in range(1<<10):
    ans=(ans+sum(dp[mask]))%MOD
print(ans)