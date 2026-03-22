n=input()
n=str(n)
n=list(n)
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        continue
    else:
        print("No")
        exit()
print("Yes")
