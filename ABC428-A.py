s,a,b,x=map(int,input().split())
time=0
time+=s*(x//(a+b))*a
#print(time)
if x%(a+b)<a:
    time+=s*(x%(a+b))
else:
    time+=s*a
print(time)