n,m = map(int,input().split())
s = input()
muji=m
logo=0
bought=0
for i in range(n):
    # print(i)
    # print("bought:"+str(bought))
    # print("logo:"+str(logo))
    # print("muji:"+str(muji))
    if s[i]=="0":
        logo=bought
        muji=m
    elif s[i]=="1":
        if muji==0:
            if logo==0:
                bought+=1
            else:
                logo-=1
        else:
            muji-=1
    elif s[i]=="2":
        if logo==0:
            bought+=1
        else:
            logo-=1
print(bought)