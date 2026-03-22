k=input()
s=input()
t=input()
count=0
idx=-1
if len(t)==len(s):
    for i in range(len(t)):
        if t[i]!=s[i]:
            count+=1
    if count<2:
        print("Yes")
    else:
        print("No")
elif len(t)==len(s)+1:
    for i in range(len(s)):
        if t[i]==s[i]:
            count+=1
        else:
            idx=i
            break
    if idx ==-1:
        idx=len(s)
    if t[:idx]+t[idx+1:] == s:
        print("Yes")
    else:
        print("No")
elif len(s)==len(t)+1:
    for i in range(len(t)):
        if s[i]==t[i]:
            count+=1
        else:
            idx=i
            break
    if idx ==-1:
        idx=len(t)
    if s[:idx]+s[idx+1:] == t:
        print("Yes")
    else:
        print("No")
else:
    print("No")
                