s=input()
bidx=[]
ridx=[]
for i in range(8):
    if s[i]=="K":
        kidx=i
    if s[i]=="Q":
        qidx=i
    elif s[i]=="R":
        ridx.append(i)
    elif s[i]=="B":
        bidx.append(i)
if (bidx[0]%2 != bidx[1]%2) and ridx[0]<kidx and ridx[1]>kidx:
    print("Yes")
else:
    print("No")