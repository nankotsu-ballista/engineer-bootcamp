a,b=map(int,input().split())
l=0
r=10**18+1
while r-l>2:
    nl,nr=l+(r-l)//3,l+(2*(r-l)//3)
    lval=nl*b+(a/(1+nl)**(0.5))
    rval=nr*b+(a/(1+nr)**(0.5))
    if lval<rval:
        r=nr
    elif lval>=rval:
        l=nl
#print(l,r)
ans=10**18
for i in range(l,r+1):
    ans=min(i*b+(a/(1+i)**(0.5)),ans)
#print(ans)
# format()メソッドの使用例
formatted_number = "{:.7f}".format(ans)
print(formatted_number)  # 出力: 123.46