import bisect
n,t=map(int,input().split())
if n==0:
    print(t)
    exit()
if n==1:
    if a[0]+100>t:
        print(a[0])
    else:
        print(t-100)
    exit()
a=list(map(int,input().split()))
sumtime=a[0]
closetime=a[0]
for i in range(1,n):
    if a[i]<=closetime+100:
        continue
    else:
        sumtime+=(a[i]-(closetime+100))
        closetime=a[i]
    #print(closetime)
if closetime+100>t:
    print(sumtime)
else:
    print(t-(closetime+100)+sumtime)
    
    