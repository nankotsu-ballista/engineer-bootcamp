import math
a,b,c=map(int,input().split())
g=math.gcd(a,b,c)
ans=0
ans+=(a//g)-1
ans+=(b//g)-1
ans+=(c//g)-1
print(ans)