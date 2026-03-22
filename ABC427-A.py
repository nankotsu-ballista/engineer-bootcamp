s=input()
t=len(s)//2
s=list(s)
ss=s[:t]+s[t+1:]
#print(ss)
result = ''.join(ss)
print(result)