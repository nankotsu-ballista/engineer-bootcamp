def sinsuu(a,sinhou):
    u=""
    while a!=0:
        u=u+str(a%sinhou)
        a=a//sinhou
    return int(u[::-1])
    
    
numbers=[]
n=int(input())
if n==0:
    print(0)
    exit()
elif n ==1:
    print(0)
    exit()
n-=1
count=0
S=sinsuu(n,5)
print(S*2)


