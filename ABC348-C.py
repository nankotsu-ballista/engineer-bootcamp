from collections import defaultdict
n=int(input())
beans = defaultdict(lambda: float('inf'))
for _ in range(n):
    a, c = map(int, input().split())
    beans[c] = min(beans[c], a)
#print(beans)
c_list = list(beans.values())
print(max(c_list))
#print(beans)