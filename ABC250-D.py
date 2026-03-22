from functools import lru_cache
import math,bisect,heapq
from collections import deque,defaultdict
n=int(input())
N = 10**6
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
limit = int(N ** 0.5)
for p in range(2, limit + 1):
    if is_prime[p]:
        for multiple in range(p * p, N + 1, p):
            is_prime[multiple] = False
primes = {i for i, ok in enumerate(is_prime) if ok}
primes =list(primes)
primes.sort()
count=0
for i in range(len(primes)):
    if primes[i]>n:
        break
    for k in range(0,i):
        #print(primes[i],primes[k],primes[i]**3*primes[k])
        if primes[i]**3*primes[k]>n:
            break
        else:
            count+=1
print(count)