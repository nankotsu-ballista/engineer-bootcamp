x,y=map(str,input().split())
a=["Ocelot", "Serval", "Lynx"]
if x==y:
    print("Yes")
    exit()
if (x==a[2] and y==a[1]) or (x==a[2] and y==a[0]):
    print("Yes")
    exit()
if (x==a[1] and y==a[0]):
    print("Yes")
    exit()
print("No")
    