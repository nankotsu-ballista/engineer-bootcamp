from functools import lru_cache
n=int(input())
if n==0:
    print(1)
    exit()
@lru_cache
def f(a):
    if a==0:
        return 1
    return f(a//2)+f(a//3)
print(f(n))