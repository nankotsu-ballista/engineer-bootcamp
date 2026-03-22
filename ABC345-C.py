s = input()
N= len(s)
count=N*(N-1)
#print(count)
from collections import Counter

counter = Counter(s)

# 英小文字のカウント
lower_counts = [counter[c] for c in 'abcdefghijklmnopqrstuvwxyz']
#print(lower_counts)
sum= 0
for i in range(26):
    sum+=lower_counts[i]*(lower_counts[i]-1)
#print(count)
#print(sum)
a=(count-sum)//2
if max(counter.values()) > 1:
    a+=1
print(a)
