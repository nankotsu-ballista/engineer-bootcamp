h,w=map(int,input().split())
ans=0
for i in range(h):
    s=list(map(str,input().strip()))
    sum=0
    for k in range(w):
        if s[k]=="T":
            sum+=1
            if sum==2:
                s[k-1]="P"
                s[k]="C"
                sum=0
        else:
            sum=0
    print("".join(s))
        