n=int(input())
H=list(map(int,input().split()))
count=0
check=0
for i in range(n):
    a=H[i]//5
    count+=a*3
    H[i]-=a*5
    while H[i]>0:
        count+=1
        if count%3 == 0:
            H[i]-=3
        else:
            H[i]-=1
print(count)
        
        