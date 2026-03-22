s=input()
t=input()
s=list(s)
t=list(t)
# print(s)
# print(t)
tmps=s[len(s)-len(t):]
#print(tmps)
diffset=set()
for i in range(len(t)):
    if tmps[i]=="?" or t[i]=="?" or(tmps[i]==t[i]):
        continue
    else:
        diffset.add(i)
if len(diffset)!=0:
    print("No")
else:
    print("Yes")
for idx in range(len(t)):
    tmps[idx]=s[idx]
    if idx in diffset:
        diffset.discard(idx)
    if tmps[idx]=="?" or t[idx]=="?" or(tmps[idx]==t[idx]):
        op=1
    else:
        diffset.add(idx)
    if len(diffset)!=0:
        print("No")
    else:
        print("Yes")

    