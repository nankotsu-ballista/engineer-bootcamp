N = 10**3
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
limit = int(N ** 0.5)
for p in range(2, limit + 1):
    if is_prime[p]:
        for multiple in range(p * p, N + 1, p):
            is_prime[multiple] = False
primes = {i for i, ok in enumerate(is_prime) if ok}
primes=list(primes)
primes.sort()
n,m=map(int,input().split())
A=list(map(int,input().split()))
s=set()
for i in range(1,m+1):
    s.add(i)
yakusu=set()
for i in A:
    k=0
    while i!=1 and k!=len(primes):
        if i%primes[k]==0:
            i//=primes[k]
            yakusu.add(primes[k])
        else:
            k+=1
    if i!=1:
        yakusu.add(i)
#print(yakusu)
for i in yakusu:
    k=1
    while k*i<=m:
        s.discard(k*i)
        k+=1
print(len(s))
s=list(s)
s.sort()
for i in s:
    print(i)
        
    
    
    