a,b=map(int,input().split())
time=0
while True:
    if a>b:
        if a%b==0:
            time+=(a//b)-1
            print(time)
            break
        time+=(a//b)
        a=a%b
    elif a<b:
        if b%a==0:
            time+=(b//a)-1
            print(time)
            break
        time+=(b//a)
        b=b%a
    else:
        print(time)
        break