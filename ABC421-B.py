x,y=map(int,input().split())
no1=x
no2=y
for i in range(8):
    ans=no1+no2
    ans=str(ans)
    ans=ans[::-1]
    count=0
    while ans[count] == "0":
        count+=1
    ans=int(ans[count:])
    no1=no2
    no2=ans
print(ans)