from functools import cache
@cache
def dfs(num,kakuritu):
    if num>n:
        return 0
    if num==n:
        return kakuritu
    s=0
    inv5 = pow(5, mod-2, mod)
    for i in range(2,7):
        s=(s+dfs(num*i,kakuritu)*inv5)%mod
    return s
n=int(input())
mod=998244353
print(dfs(1,1))

        