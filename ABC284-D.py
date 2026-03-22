N = 10**7
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False
limit = int(N ** 0.5)
for p in range(2, limit + 1):
    if is_prime[p]:
        for multiple in range(p * p, N + 1, p):
            is_prime[multiple] = False
primes = {i for i, ok in enumerate(is_prime) if ok}
t=int(input())
for ct in range(t):
    n=int(input())
    check=False
    for i in primes:
      if check==True:
        break
      if n%i!=0:
          continue
      nijou=n//i
      root=nijou**(0.5)
      if int(root)**2==nijou and i!= root:
          print(int(root),i)
          check=True
      if check==True:
        break
      if n%(i*i)==0:
        print(i,n//(i*i))
        check=True

    

    