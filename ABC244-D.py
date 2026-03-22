from collections import deque
import math
s1,s2,s3=map(str,input().split())
t1,t2,t3=map(str,input().split())
coutn=0
if s1==t1:
    coutn+=1
if s2==t2:
    coutn+=1
if s3==t3:
    coutn+=1
if coutn==1:
    print("No")
else:
    print("Yes")