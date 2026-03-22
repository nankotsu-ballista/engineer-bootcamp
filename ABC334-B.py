a,m,l,r=map(int,input().split())
l=l-a
r=r-a
if l%m==0:
    leftest=l
else:
    leftest=m*((l//m)+1)
#print(leftest)
if r%m==0:
    rightest=r
else:
    rightest=m*((r//m))
#print(rightest)
if rightest<leftest:
    print(0)
    exit()
if rightest==leftest:
    if rightest%m==0:
        print(1)
    else:
        print(0)
    exit()
print(1+((rightest-leftest)//m))