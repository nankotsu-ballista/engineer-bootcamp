n=int(input())
s=list(input())
#print(s)
n=n-len(s)
maru=[]
for i in range(n):
    maru.append("o")
ans=maru+s
print("".join(ans))
    