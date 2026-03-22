from collections import defaultdict
se=set()
defa=defaultdict(int)
s=list(input())
for i in s:
    defa[i]+=1
#print(defa)
maxi=-1
to_delet=set()
for key, value in defa.items():
    maxi=max(maxi,value)
for key, value in defa.items():
    if value==maxi:
        to_delet.add(key)
#(to_delet)
ans=[]
for i in s:
    if i not in to_delet:
        ans.append(i)
print("".join(ans))
