from itertools import permutations
M=int(input())
S1=input()
S1=list(S1+S1+S1)
S2=input()
S2=list(S2+S2+S2)
S3=input()
S3=list(S3+S3+S3)
S=[S1,S2,S3]
#print(S)
num=[0,1,2,3,4,5,6,7,8,9]
ans=1000
l=[0,1,2]
for a in permutations(l):
    for b in num:
        tempo=0
        qs=[500,500,500]
        for i in range(3):
            tmp=10**10
            St=S[a[i]]
            for j in range(tempo,len(St)):
                if St[j]==str(b):
                    qs[i]=j
                    tempo=j+1
                    break
        if qs:
            ans=min(ans,max(qs))
if ans != 500:
    print(ans)
else:
    print(-1)
