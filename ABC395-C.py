from collections import defaultdict
positions = defaultdict(list)
n=int(input())
A=list(map(int,input().split()))
for i,val in enumerate(A):
    positions[val].append(i)
minimum=10**10+1
for val in positions:
    idx_list = positions[val]
    for i in range(1, len(idx_list)):
        diff = idx_list[i] - idx_list[i - 1]
        minimum=min(minimum,diff)
if minimum==10**10+1:
    print(-1)
else:
    print(minimum+1)