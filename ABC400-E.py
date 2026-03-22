from sortedcontainers import SortedList
q=int(input())
soinsu=[0]*(10**6+1)
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

primes=list(primes)
primes.sort()
for i in primes:
    num=i
    while num<=10**6:
        soinsu[num]+=1
        num+=i
s = SortedList([])
for i in range(10**6+1):
    if soinsu[i]==2:
        s.add(i**2)
#print(anss)


for i in range(q):
    num = int(input())
    idx = s.bisect_right(num) - 1
    print(s[idx])