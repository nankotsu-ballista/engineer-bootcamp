S=input()
count=0
tidx=[]
for i in range(len(S)):
    if  S[i]=="t":
        tidx.append(i)
#print(tidx)
maxvalue=0
for i in range(len(tidx)-1):
    for j in range(i+1,len(tidx)):
        bunbo=tidx[j]-tidx[i]-1
        #print(bunbo)
        if bunbo == 0:
            continue
        bunshi=j-i-1
        tempo=bunshi/bunbo


        #print(maxvalue)
        maxvalue=max(maxvalue,tempo)
print(maxvalue)
        
        