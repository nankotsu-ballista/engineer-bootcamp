n=int(input())
s=[""]*n
for i in range(n):
    s[i]=str(input())
x,y=input().split()
x=int(x)
if s[x-1]==y:
    print("Yes")
else:
    print("No")
    