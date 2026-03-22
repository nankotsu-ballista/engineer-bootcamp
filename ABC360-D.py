import bisect
n,t=map(int,input().split())
s=input()
x=list(map(int,input().split()))
Rants=[]
Lants=[]
for i in range(n):
    if s[i]=="1":
        Rants.append(x[i])
    else:
        Lants.append(x[i])
Rants.sort()
Lants.sort()
# print(Rants)
# print(Lants)
summer=0
for i in range(len(Rants)):
    a=bisect.bisect_left(Lants,Rants[i]+(2*t)+0.1)
    b=bisect.bisect_left(Lants,Rants[i])
    # print(a)
    # print(b)
    summer+=(a-b)
print(summer)