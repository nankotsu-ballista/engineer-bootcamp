from collections import deque
import math
n,a,b=map(int,input().split())
t1=((a+(a*(n//a)))*(n//a)//2)
t2=((b+(b*(n//b)))*(n//b)//2)
c=(math.lcm(a, b))
t3=0
#print(c)
t3=((c+(c*(n//c)))*(n//c)//2)
su=((1+n)*n)//2
#print(t1,t2,t3,su)
print(su-t1-t2+t3)