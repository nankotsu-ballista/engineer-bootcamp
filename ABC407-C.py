S=input()
a=len(S)
count=a
for i in range(a-1):
    b = (10 + int(S[i]) - int(S[i+1])) % 10
    count+=b
print(count+int(S[a-1]))