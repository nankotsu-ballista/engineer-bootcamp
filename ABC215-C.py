from itertools import permutations
S,K=input().split()
K=int(K)
se=set()
for s in permutations(S):
    st = ''.join(s)
    se.add(st)
se=list(se)
se.sort()
print(se[K-1])