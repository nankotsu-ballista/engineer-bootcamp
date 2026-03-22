from collections import deque
n=int(input())
s=input()
s=list(s)
s.reverse()
ans=deque()
ans.append(n)
for i in range(n):
    if s[i]=="L":
        ans.append(n-i-1)
    if s[i]=="R":
        ans.appendleft(n-i-1)
print(*ans)