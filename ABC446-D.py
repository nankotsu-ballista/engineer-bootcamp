from collections import defaultdict
n=int(input())
A=list(map(int,input().split()))
matsubi=defaultdict(int)
s=set()
for i in A:
    matsubi[i]=max(matsubi[i],matsubi[i-1]+1)
    s.add(i)
print(max(matsubi.values()))