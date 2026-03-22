n,k=map(int,input().split())
A=list(map(int,input().split()))
maxa=max(A)
numcount=[0]*(max(A)+2)
for i in A:
    numcount[i]+=1
#print(numcount)
faccount=[0]*(maxa+2)
for i in range(1,maxa+1):
    for d in range(((maxa+1)//i)+1):
        faccount[i]+=numcount[i*d]
        #print(i,i*d)
#print(faccount)
maxfaccount=[0]*(maxa+2)
for i in range(1,maxa+1):
    if faccount[i]<k:
        continue
    for d in range(1,((maxa+1)//i)+1):
        maxfaccount[i*d]=i
#print(maxfaccount)
for i in A:
    print(maxfaccount[i])
        
    