import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)
n,a,x,y=map(int,input().split())
@lru_cache(None)
def dfs(m):
    if m==0:
        return 0
    costA=x+dfs(m//a)
    s=0
    for i in range(2,7):
        s+=dfs(m//i)
    costB=(6*y+s)/5
    return min(costA,costB)
print(dfs(n))