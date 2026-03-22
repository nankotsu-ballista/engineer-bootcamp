s=input()
t=input()
t=t.lower()
#print(t)
i=0
j=0
count=0
xcode=[]
while j<len(s) and i<len(t) and count!=len(t):
    if t[i]==s[j]:
        xcode.append(t[i])
        i+=1
        j+=1
        count+=1
    elif t[i]!=s[j]:
        j+=1
xcode.append("x")
#(xcode)
xa = ''.join(xcode)
if count ==len(t):
    print("Yes")
else:
    if t == xa:
        print("Yes")
    else:
        print("No")