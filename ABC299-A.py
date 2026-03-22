n=int(input())
s=input()
idx=[]
for i in range(n):
    if s[i]=="|":
        idx.append(i)
    if s[i]=="*":
        index=i
if idx[0]<index<idx[1]:
    print("in")
else:
    print("out")