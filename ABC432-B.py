x=str(input())
x=list(x)
x.sort()
#print(x)
zeros=""
ans=""
for i in x:
    if i=="0":
        zeros=zeros+"0"
    else:
        ans=ans+i
# print(ans)
# print(zeros)
print(ans[0]+zeros+ans[1:])