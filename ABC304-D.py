from collections import defaultdict
import bisect              
w,h=map(int,input().split())
n=int(input())
q=[]
cnt = defaultdict(int)        # デフォルト0（カウント用）
for i in range(n):
    w,h=map(int,input().split())
    q.append((w,h))
A=int(input())
a=list(map(int,input().split()))
B=int(input())
b=list(map(int,input().split()))
for i in range(n):
    w,h=q[i]
    x=bisect.bisect_right(a, w)
    y=bisect.bisect_right(b, h)
    cnt[(x, y)] += 1              # または cnt[a, b] += 1 でも同じ（タプル扱い）
if len(cnt)<(A+1)*(B+1):
    print("0"+" "+str(max(cnt.values())))
else:
    print(str(min(cnt.values()))+" "+str(max(cnt.values())))