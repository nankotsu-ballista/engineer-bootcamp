n,r,c=map(int,input().split())
s=input()
ans=[]
fr,fc=0,0
seen=set()
seen.add((0,0))
for i in range(n):
    if s[i]=="N":
        r +=1
        fr +=1
    elif s[i]=="W":
        c+=1
        fc+=1
    elif s[i]=="E":
        c-=1
        fc-=1
    elif s[i]=="S":
        r -=1
        fr -=1
    seen.add((fr,fc))
    if (r,c) in seen:
        ans.append("1")
    else:
        ans.append("0")
    # print(seen)
    # print(str(r)+" "+str(c))
print(''.join(ans))