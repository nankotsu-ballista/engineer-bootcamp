s=input()
s=list(s)
i=0
while i<len(s)-1:
    if s[i]=="W" and s[i+1]=="A":
        s[i]="A"
        s[i+1]="C"
        i = max(i - 1, 0) 
    else:
        i+=1
print("".join(str(x) for x in s))