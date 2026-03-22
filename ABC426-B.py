S=input()
S=list(S)
#print(S)
teisu=-1
count=0
for i in range(len(S)):
    if i==0:
        continue
    if S[i]==S[0]:
        count=1
    else:
        teisu=i
    #print(i)
if count == 1:
    print(S[teisu])
else:
    print(S[0])

        
        
        