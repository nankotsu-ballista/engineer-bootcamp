n=int(input())
S=input()
count=0
if n<3:
    print("No")
    exit()
if S[-1]=="a":
    count+=1
if S[-2]=="e":
    count+=1
if S[-3]=="t":
    count+=1
if count==3:
    print("Yes")
else:
    print("No")