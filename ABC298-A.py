n=int(input())
s=input()
check=False
for i in range(n):
    if s[i]=="x":
        print("No")
        exit()
    elif s[i]=="o":
        check=True
if check==True:
    print("Yes")
else:
    print("No")